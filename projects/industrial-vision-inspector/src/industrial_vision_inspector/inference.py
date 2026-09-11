from __future__ import annotations

import json
from pathlib import Path

import cv2
import numpy as np
import torch
from PIL import Image

from .data import build_transforms
from .image_ops import compute_quality_metrics, read_grayscale
from .models import build_model


def predict_image(checkpoint_path: str | Path, image_path: str | Path) -> dict[str, object]:
    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False); classes = list(checkpoint["classes"])
    model = build_model(str(checkpoint["model_name"]), len(classes), pretrained=False); model.load_state_dict(checkpoint["state_dict"]); model.eval()
    gray = read_grayscale(image_path); quality = compute_quality_metrics(gray).to_dict(); transform = build_transforms(int(checkpoint["image_size"]), train=False, use_cv_preprocess=bool(checkpoint["use_cv_preprocess"])); tensor = transform(Image.fromarray(gray, mode="L")).unsqueeze(0)
    with torch.inference_mode(): probs = torch.softmax(model(tensor), dim=1)[0].cpu().numpy()
    order = np.argsort(-probs); ranked = [{"class": classes[int(i)], "probability": float(probs[int(i)])} for i in order]
    return {"image": str(image_path), "prediction": ranked[0]["class"], "confidence": ranked[0]["probability"], "ranked_probabilities": ranked, "quality": quality}


def render_result(image_path: str | Path, result: dict[str, object], output_path: str | Path) -> Path:
    image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
    if image is None: raise ValueError(f"Could not read image: {image_path}")
    h, w = image.shape[:2]; pad = max(54, h // 5); out = np.full((h + pad, w, 3), 245, dtype=np.uint8); out[pad:, :] = image
    label = f"{result['prediction']}  {float(result['confidence']) * 100:.1f}%"; cv2.putText(out, label, (8, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20, 20, 20), 2, cv2.LINE_AA)
    quality = result["quality"]; cv2.putText(out, f"sharpness={float(quality['sharpness_laplacian_var']):.1f}  edge_density={float(quality['edge_density']):.3f}", (8, 49), cv2.FONT_HERSHEY_SIMPLEX, 0.46, (50, 50, 50), 1, cv2.LINE_AA)
    target = Path(output_path); target.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(target), out): raise RuntimeError(f"Could not write {target}")
    return target


def save_json(result: dict[str, object], path: str | Path) -> Path:
    target = Path(path); target.parent.mkdir(parents=True, exist_ok=True); target.write_text(json.dumps(result, indent=2), encoding="utf-8"); return target
