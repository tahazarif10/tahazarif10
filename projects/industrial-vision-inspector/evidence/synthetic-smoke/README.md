# Synthetic smoke verification

This record proves that the software path executes end-to-end. It is **not** a real-dataset benchmark.

Verified locally on CPU with Python 3.13.5, PyTorch 2.10.0+cpu, torchvision 0.25.0+cpu, OpenCV 4.13.0 and scikit-learn 1.8.0.

Checks performed:

- `pytest`: **7/7 passed**
- deterministic six-class synthetic dataset generation
- TinyConvNet training for 8 epochs
- held-out synthetic test accuracy: **0.9722**
- held-out synthetic macro F1: **0.9720**
- single-image inference on a synthetic `scratches` sample: predicted `scratches` at **0.8674** confidence
- training history, confusion-matrix rendering, JSON metrics, checkpoint save/load, and annotated prediction rendering completed successfully

These numbers are intentionally excluded from resume performance claims because the data are procedural smoke-test images rather than real manufacturing imagery.
