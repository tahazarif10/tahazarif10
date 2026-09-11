from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path

import cv2
import numpy as np


@dataclass(frozen=True)
class ImageQuality:
    brightness_mean: float
    contrast_std: float
    sharpness_laplacian_var: float
    edge_density: float
    entropy_bits: float

    def to_dict(self) -> dict[str, float]:
        return asdict(self)


def read_grayscale(path: str | Path) -> np.ndarray:
    image = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Could not read image: {path}")
    return image


def compute_quality_metrics(image: np.ndarray) -> ImageQuality:
    if image.ndim == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if image.ndim != 2 or image.size == 0:
        raise ValueError("Expected a non-empty grayscale or BGR image")
    image_u8 = np.clip(image, 0, 255).astype(np.uint8, copy=False)
    brightness = float(np.mean(image_u8))
    contrast = float(np.std(image_u8))
    sharpness = float(cv2.Laplacian(image_u8, cv2.CV_64F).var())
    edges = cv2.Canny(image_u8, 75, 150)
    edge_density = float(np.count_nonzero(edges) / edges.size)
    hist = cv2.calcHist([image_u8], [0], None, [256], [0, 256]).ravel().astype(np.float64)
    probs = hist / max(hist.sum(), 1.0)
    probs = probs[probs > 0.0]
    entropy = float(-(probs * np.log2(probs)).sum())
    return ImageQuality(brightness, contrast, sharpness, edge_density, entropy)


def preprocess_grayscale(image: np.ndarray, *, clahe_clip: float = 2.0) -> np.ndarray:
    if image.ndim == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if image.ndim != 2 or image.size == 0:
        raise ValueError("Expected a non-empty grayscale or BGR image")
    image_u8 = np.clip(image, 0, 255).astype(np.uint8, copy=False)
    clahe = cv2.createCLAHE(clipLimit=float(clahe_clip), tileGridSize=(8, 8))
    enhanced = clahe.apply(image_u8)
    return cv2.medianBlur(enhanced, 3)
