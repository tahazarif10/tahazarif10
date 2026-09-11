# Dataset protocol

## Primary real-data target: NEU-CLS

The official Northeastern University surface-defect database provides an image-only `NEU-CLS` variant for classification. Public descriptions report 1,800 grayscale 200x200 images across six hot-rolled steel surface-defect classes, 300 per class.

This repository does not contain those images.

## Preparation protocol

```bash
ivi prepare-neu --source <raw-neu-cls> --output <prepared-directory> --seed 42
```

Default class-stratified split: 70% train, 15% validation, 15% test. For 300 images per class this is approximately 210/45/45 per class.

The manifest records a SHA-256 digest for every copied image.

## Leakage controls

- files are assigned to exactly one split
- split generation occurs independently inside each class
- evaluation checks class-order compatibility
- the test set is not used to select the checkpoint

## Synthetic dataset

The built-in procedural dataset exists only for unit tests, smoke tests, CI, and end-to-end software verification. It is not a substitute for real defect imagery and its metrics must not be advertised as industrial accuracy.
