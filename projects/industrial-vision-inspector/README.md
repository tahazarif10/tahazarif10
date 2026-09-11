# Industrial Vision Inspector

A reproducible **Python + OpenCV + PyTorch** portfolio project for industrial surface-defect inspection.

The project deliberately separates two things that are often blurred together:

1. **Classical image processing** — deterministic quality metrics and contrast/denoise preprocessing.
2. **Machine learning** — a train/evaluate/infer pipeline for multi-class surface-defect classification.

It is designed around the public **NEU-CLS steel-surface defect classification dataset**, while keeping the repository itself dataset-free. The official Northeastern University database describes six hot-rolled steel defect classes and provides NEU-CLS for classification. The code also contains a deterministic synthetic generator used only for tests and pipeline smoke checks.

> **Evidence boundary:** synthetic-data results validate software plumbing only. They are not manufacturing-performance evidence and must not be reported as real-world model accuracy.

## What this demonstrates

- Python package design and command-line tooling
- OpenCV image preprocessing and image-quality measurements
- PyTorch CNN training and inference
- optional ResNet-18 transfer-learning path
- deterministic train/validation/test preparation for NEU-CLS
- SHA-256 data manifest generation for reproducibility
- accuracy, macro precision, macro recall, macro F1 and confusion-matrix evaluation
- checkpointed single-image inference with ranked probabilities
- unit tests and GitHub Actions CI

## Architecture

```text
Raw image
   │
   ├── Classical CV metrics
   │      brightness · contrast · sharpness · edges · entropy
   │
   └── CLAHE + median denoise
              │
              v
         normalized tensor
              │
      ┌───────┴────────┐
      │                │
  TinyConvNet       ResNet-18
  smoke/CI          portfolio training
      │                │
      └───────┬────────┘
              v
     class probabilities
              │
      metrics / JSON / render
```

## Supported defect classes

The NEU-CLS adapter uses these canonical labels:

- `crazing`
- `inclusion`
- `patches`
- `pitted_surface`
- `rolled_in_scale`
- `scratches`

## Quick start

Python 3.10+ is required.

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
pytest
```

### Synthetic end-to-end smoke check

```bash
ivi make-synthetic --output data/synthetic
ivi train --data data/synthetic --output artifacts/smoke --model tinycnn --epochs 8 --image-size 64
ivi infer --checkpoint artifacts/smoke/model.pt --image data/synthetic/test/scratches/scratches_0000.png --json artifacts/smoke/prediction.json --render artifacts/smoke/prediction.png
```

Or:

```bash
python scripts/run_smoke.py
```

### Prepare NEU-CLS deterministically

Download **NEU-CLS** from the official NEU surface defect database page. Do not commit the dataset into this repository.

```bash
ivi prepare-neu --source J:\datasets\NEU-CLS --output J:\datasets\NEU-CLS-split --seed 42
```

This copies images into class-stratified `train`, `val`, and `test` folders and writes `manifest.csv` containing the split, class, source filename, relative path, and SHA-256 hash of every copied image.

### Train a portfolio model

```bash
ivi train --data J:\datasets\NEU-CLS-split --output artifacts\neu_resnet18 --model resnet18 --pretrained --epochs 20 --image-size 224 --batch-size 32 --learning-rate 0.0003
```

`--pretrained` uses torchvision's ImageNet weights and therefore needs the weights available in the local PyTorch cache or network access on first use.

### Evaluate and infer

```bash
ivi evaluate --checkpoint artifacts\neu_resnet18\model.pt --data J:\datasets\NEU-CLS-split --split test --output artifacts\neu_resnet18
ivi infer --checkpoint artifacts\neu_resnet18\model.pt --image J:\datasets\NEU-CLS-split\test\scratches\scratches_0000.bmp --json artifacts\neu_resnet18\single_prediction.json --render artifacts\neu_resnet18\single_prediction.png
```

## Reproducibility choices

- deterministic Python/NumPy/PyTorch seeds
- fixed class mapping
- class-stratified split generation
- original raw images are copied, not edited in place
- SHA-256 manifest for prepared real data
- preprocessing configuration stored in the checkpoint
- model class order stored in the checkpoint and checked at evaluation time
- best validation-loss state retained for final evaluation

## Dataset and licensing note

The dataset is intentionally **not redistributed here**. Use the official NEU surface defect database source and verify the terms supplied with the dataset before redistributing any images.

Official source: `https://faculty.neu.edu.cn/songkc/en/zdylm/263265/list/`

## Project status

**v0.1:** software pipeline complete and locally verified. Real NEU-CLS benchmark metrics are intentionally not claimed until the real dataset is prepared and training is executed on the target machine.

See `docs/MODEL_CARD.md`, `docs/DATASET.md`, and `docs/ARCHITECTURE.md` for evidence boundaries and design details.