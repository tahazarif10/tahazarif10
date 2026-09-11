# Architecture

## Goal

Provide a small but defensible industrial-computer-vision project that demonstrates Python engineering, classical image processing, and machine learning without hiding data leakage or overstating model evidence.

## Components

### Classical CV layer

`image_ops.py` computes deterministic brightness, contrast, Laplacian-variance sharpness, Canny edge density, and histogram entropy. The optional model preprocessing path applies CLAHE followed by a 3x3 median filter.

### Dataset layer

`prepare_neu_cls()` accepts canonical NEU-style filenames (`Cr_`, `In_`, `Pa_`, `PS_`, `RS_`, `Sc_`) or class folders. It creates deterministic class-stratified splits and hashes every copied file. The raw source directory is never modified.

### Model layer

- `tinycnn`: fast smoke/CI model.
- `resnet18`: torchvision architecture suitable for a stronger real-data experiment; ImageNet initialization is optional.

### Training/evaluation layer

The trainer records configuration, retains the best validation-loss checkpoint, writes epoch history, and evaluates on a separate test split. Evaluation reports accuracy, macro precision, macro recall, macro F1, confusion matrix, and per-class metrics.

### Inference layer

Single-image inference outputs ranked probabilities plus classical CV quality metrics and can render a compact annotated result image.

## Non-goals

- no production-grade quality-inspection claim
- no real-time throughput claim
- no defect localization/segmentation in v0.1
- no synthetic accuracy presented as real-data evidence
- no dataset redistribution
