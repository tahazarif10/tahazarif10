from __future__ import annotations

import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, precision_score, recall_score
from torch import nn

from .data import make_loaders
from .models import build_model


@dataclass(frozen=True)
class TrainConfig:
    data_dir: str
    output_dir: str
    model: str = "tinycnn"
    pretrained: bool = False
    image_size: int = 96
    batch_size: int = 32
    epochs: int = 5
    learning_rate: float = 1e-3
    seed: int = 42
    use_cv_preprocess: bool = True


def set_seed(seed: int) -> None:
    random.seed(seed); np.random.seed(seed); torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True; torch.backends.cudnn.benchmark = False


def _device() -> torch.device:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def _run_epoch(model, loader, criterion, optimizer, device, *, training: bool):
    model.train(training); total_loss = 0.0; total = 0; correct = 0
    for inputs, targets in loader:
        inputs, targets = inputs.to(device), targets.to(device)
        if training: optimizer.zero_grad(set_to_none=True)
        logits = model(inputs); loss = criterion(logits, targets)
        if training: loss.backward(); optimizer.step()
        total_loss += float(loss.detach().cpu()) * targets.size(0)
        correct += int((logits.argmax(dim=1) == targets).sum().detach().cpu()); total += targets.size(0)
    return total_loss / max(total, 1), correct / max(total, 1)


def train(config: TrainConfig) -> dict[str, object]:
    set_seed(config.seed); output = Path(config.output_dir); output.mkdir(parents=True, exist_ok=True)
    loaders, classes = make_loaders(config.data_dir, image_size=config.image_size, batch_size=config.batch_size, use_cv_preprocess=config.use_cv_preprocess)
    device = _device(); model = build_model(config.model, len(classes), pretrained=config.pretrained).to(device)
    criterion = nn.CrossEntropyLoss(); optimizer = torch.optim.AdamW(model.parameters(), lr=config.learning_rate, weight_decay=1e-4)
    history = []; best_val = float("inf"); best_state = None
    for epoch in range(1, config.epochs + 1):
        train_loss, train_acc = _run_epoch(model, loaders["train"], criterion, optimizer, device, training=True)
        with torch.inference_mode(): val_loss, val_acc = _run_epoch(model, loaders["val"], criterion, optimizer, device, training=False)
        history.append({"epoch": epoch, "train_loss": train_loss, "train_accuracy": train_acc, "val_loss": val_loss, "val_accuracy": val_acc})
        if val_loss < best_val:
            best_val = val_loss; best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
    if best_state is None: raise RuntimeError("Training produced no checkpoint")
    model.load_state_dict(best_state)
    checkpoint = {"format_version": 1, "model_name": config.model, "pretrained_requested": config.pretrained, "classes": classes, "image_size": config.image_size, "use_cv_preprocess": config.use_cv_preprocess, "state_dict": model.state_dict()}
    checkpoint_path = output / "model.pt"; torch.save(checkpoint, checkpoint_path)
    history_frame = pd.DataFrame(history); history_frame.to_csv(output / "history.csv", index=False); _plot_history(history_frame, output / "history.png")
    (output / "train_config.json").write_text(json.dumps(asdict(config), indent=2), encoding="utf-8")
    metrics = evaluate_checkpoint(checkpoint_path, config.data_dir, split="test", output_dir=output)
    return {"checkpoint": str(checkpoint_path), "classes": classes, "metrics": metrics, "device": str(device)}


def _predict(model, loader, device):
    model.eval(); targets_all = []; preds_all = []
    with torch.inference_mode():
        for inputs, targets in loader:
            probs = torch.softmax(model(inputs.to(device)), dim=1).cpu(); preds = probs.argmax(dim=1)
            targets_all.extend(targets.tolist()); preds_all.extend(preds.tolist())
    return targets_all, preds_all


def evaluate_checkpoint(checkpoint_path: str | Path, data_dir: str | Path, *, split: str = "test", output_dir: str | Path | None = None) -> dict[str, object]:
    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False); classes = list(checkpoint["classes"])
    loaders, current_classes = make_loaders(data_dir, image_size=int(checkpoint["image_size"]), batch_size=64, use_cv_preprocess=bool(checkpoint["use_cv_preprocess"]))
    if current_classes != classes: raise ValueError("Checkpoint class order does not match dataset class order")
    device = _device(); model = build_model(str(checkpoint["model_name"]), len(classes), pretrained=False).to(device); model.load_state_dict(checkpoint["state_dict"])
    y_true, y_pred = _predict(model, loaders[split], device)
    metrics = {"split": split, "accuracy": float(accuracy_score(y_true, y_pred)), "macro_precision": float(precision_score(y_true, y_pred, average="macro", zero_division=0)), "macro_recall": float(recall_score(y_true, y_pred, average="macro", zero_division=0)), "macro_f1": float(f1_score(y_true, y_pred, average="macro", zero_division=0)), "classes": classes, "confusion_matrix": confusion_matrix(y_true, y_pred, labels=list(range(len(classes)))).tolist(), "classification_report": classification_report(y_true, y_pred, labels=list(range(len(classes))), target_names=classes, output_dict=True, zero_division=0)}
    if output_dir is not None:
        output = Path(output_dir); output.mkdir(parents=True, exist_ok=True); (output / f"metrics_{split}.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8"); _plot_confusion_matrix(np.asarray(metrics["confusion_matrix"]), classes, output / f"confusion_matrix_{split}.png")
    return metrics


def _plot_history(frame: pd.DataFrame, output_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 4.2)); ax.plot(frame["epoch"], frame["train_accuracy"], marker="o", label="train accuracy"); ax.plot(frame["epoch"], frame["val_accuracy"], marker="o", label="validation accuracy"); ax.set_xlabel("epoch"); ax.set_ylabel("accuracy"); ax.set_ylim(0.0, 1.02); ax.grid(True, alpha=0.25); ax.legend(); fig.tight_layout(); fig.savefig(output_path, dpi=160); plt.close(fig)


def _plot_confusion_matrix(matrix: np.ndarray, classes: list[str], output_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(7.2, 6.2)); image = ax.imshow(matrix); ax.set_xticks(range(len(classes)), labels=classes, rotation=45, ha="right"); ax.set_yticks(range(len(classes)), labels=classes); ax.set_xlabel("predicted"); ax.set_ylabel("true"); ax.set_title("Confusion matrix"); threshold = float(matrix.max()) / 2.0 if matrix.size else 0.0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]): ax.text(j, i, str(int(matrix[i, j])), ha="center", va="center", color="white" if matrix[i, j] > threshold else "black")
    fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04); fig.tight_layout(); fig.savefig(output_path, dpi=160); plt.close(fig)
