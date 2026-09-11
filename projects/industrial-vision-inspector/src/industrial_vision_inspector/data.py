from __future__ import annotations

import csv
import hashlib
import random
import shutil
from pathlib import Path

from PIL import Image
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from .image_ops import preprocess_grayscale

SUPPORTED_EXTENSIONS = {".bmp", ".jpg", ".jpeg", ".png", ".tif", ".tiff"}
NEU_PREFIX_TO_CLASS = {"Cr": "crazing", "In": "inclusion", "Pa": "patches", "PS": "pitted_surface", "RS": "rolled_in_scale", "Sc": "scratches"}


class OpenCVPreprocess:
    def __call__(self, image: Image.Image) -> Image.Image:
        import numpy as np
        gray = np.asarray(image.convert("L"))
        processed = preprocess_grayscale(gray)
        return Image.fromarray(processed, mode="L").convert("RGB")


def build_transforms(image_size: int = 224, *, train: bool, use_cv_preprocess: bool = True):
    ops: list[object] = [OpenCVPreprocess() if use_cv_preprocess else transforms.Grayscale(num_output_channels=3), transforms.Resize((image_size, image_size))]
    if train:
        ops.extend([transforms.RandomHorizontalFlip(p=0.5), transforms.RandomVerticalFlip(p=0.2), transforms.RandomRotation(degrees=8)])
    ops.extend([transforms.ToTensor(), transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])])
    return transforms.Compose(ops)


def make_loaders(data_dir: str | Path, *, image_size: int = 224, batch_size: int = 32, num_workers: int = 0, use_cv_preprocess: bool = True):
    root = Path(data_dir)
    datasets_by_split = {}
    for split in ("train", "val", "test"):
        split_dir = root / split
        if not split_dir.is_dir():
            raise FileNotFoundError(f"Missing dataset split: {split_dir}")
        datasets_by_split[split] = datasets.ImageFolder(split_dir, transform=build_transforms(image_size, train=(split == "train"), use_cv_preprocess=use_cv_preprocess))
    classes = datasets_by_split["train"].classes
    for split in ("val", "test"):
        if datasets_by_split[split].classes != classes:
            raise ValueError(f"Class mismatch between train and {split}")
    loaders = {split: DataLoader(dataset, batch_size=batch_size, shuffle=(split == "train"), num_workers=num_workers, pin_memory=False) for split, dataset in datasets_by_split.items()}
    return loaders, classes


def _class_from_neu_path(path: Path) -> str:
    parent = path.parent.name.lower().replace("-", "_").replace(" ", "_")
    if parent in set(NEU_PREFIX_TO_CLASS.values()):
        return parent
    stem_prefix = path.stem.split("_")[0]
    if stem_prefix in NEU_PREFIX_TO_CLASS:
        return NEU_PREFIX_TO_CLASS[stem_prefix]
    raise ValueError(f"Could not infer NEU class for {path.name}")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def prepare_neu_cls(source_dir: str | Path, output_dir: str | Path, *, seed: int = 42, train_fraction: float = 0.70, val_fraction: float = 0.15) -> Path:
    if not (0.0 < train_fraction < 1.0 and 0.0 < val_fraction < 1.0 and train_fraction + val_fraction < 1.0):
        raise ValueError("Invalid train/validation fractions")
    source, target = Path(source_dir), Path(output_dir)
    images = [p for p in source.rglob("*") if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS]
    if not images:
        raise FileNotFoundError(f"No supported images found under {source}")
    by_class: dict[str, list[Path]] = {}
    for path in images:
        by_class.setdefault(_class_from_neu_path(path), []).append(path)
    rng = random.Random(seed)
    rows = []
    for class_name in sorted(by_class):
        class_images = sorted(by_class[class_name])
        rng.shuffle(class_images)
        n = len(class_images)
        train_end = int(round(n * train_fraction))
        val_end = train_end + int(round(n * val_fraction))
        split_groups = {"train": class_images[:train_end], "val": class_images[train_end:val_end], "test": class_images[val_end:]}
        for split, split_images in split_groups.items():
            for index, src in enumerate(split_images):
                dst_dir = target / split / class_name
                dst_dir.mkdir(parents=True, exist_ok=True)
                dst = dst_dir / f"{class_name}_{index:04d}{src.suffix.lower()}"
                shutil.copy2(src, dst)
                rows.append({"split": split, "class": class_name, "source_name": src.name, "relative_path": dst.relative_to(target).as_posix(), "sha256": _sha256(dst)})
    manifest = target / "manifest.csv"
    with manifest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["split", "class", "source_name", "relative_path", "sha256"])
        writer.writeheader(); writer.writerows(rows)
    return manifest
