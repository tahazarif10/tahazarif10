# Model Card — Industrial Vision Inspector v0.1

## Intended use

Educational/portfolio surface-defect classification experiments and software verification.

## Models

- TinyConvNet: three convolution blocks plus global average pooling.
- ResNet-18: torchvision implementation with the final classification head replaced for the dataset class count.

## Inputs

Grayscale or RGB surface images. The default path converts to grayscale, applies CLAHE and median denoising, then converts to three channels and normalizes to `[-1, 1]`.

## Outputs

A probability distribution over the configured classes, top prediction/confidence, and separate classical image-quality metrics.

## Metrics

Accuracy, macro precision, macro recall, macro F1, confusion matrix and per-class precision/recall/F1.

## Current evidence

The software pipeline and seven local tests were executed on deterministic synthetic data. No real NEU-CLS benchmark number is claimed in v0.1 until a complete real-data run is executed and retained.

## Limitations

- classifier only; it does not localize defects
- target camera/lighting may differ from the training distribution
- confidence is not calibrated for safety-critical decisions
- image-quality metrics are engineering indicators, not defect probabilities
- production deployment would require target-line validation, drift monitoring, latency measurements and false-accept/false-reject analysis
