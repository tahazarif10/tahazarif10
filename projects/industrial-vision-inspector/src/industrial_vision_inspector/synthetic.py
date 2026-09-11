from __future__ import annotations

import json
from pathlib import Path

import cv2
import numpy as np

CLASSES = ("crazing", "inclusion", "patches", "pitted_surface", "rolled_in_scale", "scratches")


def _base(rng: np.random.Generator, size: int) -> np.ndarray:
    background = rng.normal(132, 18, (size, size)).astype(np.float32)
    gradient = np.linspace(-15, 15, size, dtype=np.float32)[None, :]
    return np.clip(background + gradient, 0, 255).astype(np.uint8)


def _draw_crazing(img: np.ndarray, rng: np.random.Generator) -> None:
    h, w = img.shape
    for _ in range(10):
        pts = []
        x, y = int(rng.integers(0, w)), int(rng.integers(0, h))
        for _ in range(int(rng.integers(3, 7))):
            x = int(np.clip(x + rng.integers(-25, 26), 0, w - 1))
            y = int(np.clip(y + rng.integers(-25, 26), 0, h - 1))
            pts.append((x, y))
        if len(pts) >= 2:
            cv2.polylines(img, [np.array(pts, np.int32)], False, int(rng.integers(40, 80)), 1)


def _draw_inclusion(img: np.ndarray, rng: np.random.Generator) -> None:
    h, w = img.shape
    for _ in range(14):
        center = (int(rng.integers(10, w - 10)), int(rng.integers(10, h - 10)))
        axes = (int(rng.integers(2, 8)), int(rng.integers(1, 5)))
        cv2.ellipse(img, center, axes, float(rng.integers(0, 180)), 0, 360, int(rng.integers(25, 70)), -1)


def _draw_patches(img: np.ndarray, rng: np.random.Generator) -> None:
    h, w = img.shape
    overlay = img.copy()
    for _ in range(5):
        center = (int(rng.integers(20, w - 20)), int(rng.integers(20, h - 20)))
        axes = (int(rng.integers(12, 35)), int(rng.integers(8, 25)))
        cv2.ellipse(overlay, center, axes, float(rng.integers(0, 180)), 0, 360, int(rng.integers(165, 220)), -1)
    cv2.addWeighted(overlay, 0.55, img, 0.45, 0, dst=img)


def _draw_pits(img: np.ndarray, rng: np.random.Generator) -> None:
    h, w = img.shape
    for _ in range(28):
        center = (int(rng.integers(6, w - 6)), int(rng.integers(6, h - 6)))
        radius = int(rng.integers(2, 7))
        cv2.circle(img, center, radius, int(rng.integers(30, 95)), -1)
        cv2.circle(img, (center[0] - 1, center[1] - 1), max(1, radius // 2), int(rng.integers(160, 220)), -1)


def _draw_scale(img: np.ndarray, rng: np.random.Generator) -> None:
    h, w = img.shape
    for y in range(0, h, int(rng.integers(10, 18))):
        cv2.line(img, (0, y), (w - 1, min(h - 1, y + int(rng.integers(-4, 5)))), int(rng.integers(65, 105)), int(rng.integers(2, 5)))
    blur = cv2.GaussianBlur(img, (9, 1), 0)
    cv2.addWeighted(img, 0.55, blur, 0.45, 0, dst=img)


def _draw_scratches(img: np.ndarray, rng: np.random.Generator) -> None:
    h, w = img.shape
    for _ in range(5):
        x1 = int(rng.integers(0, w // 3))
        y1 = int(rng.integers(0, h))
        x2 = int(rng.integers(2 * w // 3, w))
        y2 = int(np.clip(y1 + rng.integers(-30, 31), 0, h - 1))
        cv2.line(img, (x1, y1), (x2, y2), int(rng.integers(215, 250)), int(rng.integers(1, 3)))


DRAWERS = {"crazing": _draw_crazing, "inclusion": _draw_inclusion, "patches": _draw_patches, "pitted_surface": _draw_pits, "rolled_in_scale": _draw_scale, "scratches": _draw_scratches}


def make_image(class_name: str, *, seed: int, size: int = 200) -> np.ndarray:
    if class_name not in DRAWERS:
        raise ValueError(f"Unknown synthetic class: {class_name}")
    rng = np.random.default_rng(seed)
    image = _base(rng, size)
    DRAWERS[class_name](image, rng)
    return cv2.GaussianBlur(image, (3, 3), 0)


def generate_dataset(output_dir: str | Path, *, train_per_class: int = 48, val_per_class: int = 12, test_per_class: int = 12, seed: int = 42, size: int = 200) -> Path:
    root = Path(output_dir)
    counts = {"train": train_per_class, "val": val_per_class, "test": test_per_class}
    counter = 0
    for split, count in counts.items():
        for class_name in CLASSES:
            class_dir = root / split / class_name
            class_dir.mkdir(parents=True, exist_ok=True)
            for index in range(count):
                image = make_image(class_name, seed=seed + counter * 1009 + index, size=size)
                target = class_dir / f"{class_name}_{index:04d}.png"
                if not cv2.imwrite(str(target), image):
                    raise RuntimeError(f"Failed to write {target}")
            counter += 1
    metadata = {"purpose": "deterministic smoke-test data; not real manufacturing evidence", "classes": list(CLASSES), "counts_per_class": counts, "seed": seed, "size": size}
    (root / "SYNTHETIC_DATASET.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    return root
