from pathlib import Path
import shutil

from industrial_vision_inspector.engine import TrainConfig, train
from industrial_vision_inspector.inference import predict_image, render_result
from industrial_vision_inspector.synthetic import generate_dataset


def main() -> None:
    root = Path(".smoke")
    if root.exists(): shutil.rmtree(root)
    data = generate_dataset(root / "data", train_per_class=48, val_per_class=12, test_per_class=12, seed=42, size=128)
    result = train(TrainConfig(data_dir=str(data), output_dir=str(root / "artifacts"), model="tinycnn", image_size=64, batch_size=32, epochs=8, seed=42))
    sample = next((data / "test" / "scratches").glob("*.png")); prediction = predict_image(root / "artifacts" / "model.pt", sample); render_result(sample, prediction, root / "artifacts" / "sample_prediction.png")
    print({"accuracy": result["metrics"]["accuracy"], "macro_f1": result["metrics"]["macro_f1"], "prediction": prediction["prediction"], "confidence": prediction["confidence"]})


if __name__ == "__main__": main()
