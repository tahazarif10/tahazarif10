from __future__ import annotations

import argparse
import json

from .data import prepare_neu_cls
from .engine import TrainConfig, evaluate_checkpoint, train
from .image_ops import compute_quality_metrics, read_grayscale
from .inference import predict_image, render_result, save_json
from .synthetic import generate_dataset


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ivi", description="Industrial Vision Inspector"); sub = parser.add_subparsers(dest="command", required=True)
    synth = sub.add_parser("make-synthetic"); synth.add_argument("--output", required=True); synth.add_argument("--train-per-class", type=int, default=48); synth.add_argument("--val-per-class", type=int, default=12); synth.add_argument("--test-per-class", type=int, default=12); synth.add_argument("--seed", type=int, default=42)
    neu = sub.add_parser("prepare-neu"); neu.add_argument("--source", required=True); neu.add_argument("--output", required=True); neu.add_argument("--seed", type=int, default=42)
    tr = sub.add_parser("train"); tr.add_argument("--data", required=True); tr.add_argument("--output", required=True); tr.add_argument("--model", choices=["tinycnn", "resnet18"], default="tinycnn"); tr.add_argument("--pretrained", action="store_true"); tr.add_argument("--image-size", type=int, default=96); tr.add_argument("--batch-size", type=int, default=32); tr.add_argument("--epochs", type=int, default=5); tr.add_argument("--learning-rate", type=float, default=1e-3); tr.add_argument("--seed", type=int, default=42); tr.add_argument("--no-cv-preprocess", action="store_true")
    ev = sub.add_parser("evaluate"); ev.add_argument("--checkpoint", required=True); ev.add_argument("--data", required=True); ev.add_argument("--split", choices=["train", "val", "test"], default="test"); ev.add_argument("--output")
    inf = sub.add_parser("infer"); inf.add_argument("--checkpoint", required=True); inf.add_argument("--image", required=True); inf.add_argument("--json"); inf.add_argument("--render")
    quality = sub.add_parser("quality"); quality.add_argument("--image", required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "make-synthetic": print(generate_dataset(args.output, train_per_class=args.train_per_class, val_per_class=args.val_per_class, test_per_class=args.test_per_class, seed=args.seed))
    elif args.command == "prepare-neu": print(prepare_neu_cls(args.source, args.output, seed=args.seed))
    elif args.command == "train": print(json.dumps(train(TrainConfig(data_dir=args.data, output_dir=args.output, model=args.model, pretrained=args.pretrained, image_size=args.image_size, batch_size=args.batch_size, epochs=args.epochs, learning_rate=args.learning_rate, seed=args.seed, use_cv_preprocess=not args.no_cv_preprocess)), indent=2))
    elif args.command == "evaluate": print(json.dumps(evaluate_checkpoint(args.checkpoint, args.data, split=args.split, output_dir=args.output), indent=2))
    elif args.command == "infer":
        result = predict_image(args.checkpoint, args.image)
        if args.json: save_json(result, args.json)
        if args.render: render_result(args.image, result, args.render)
        print(json.dumps(result, indent=2))
    elif args.command == "quality": print(json.dumps(compute_quality_metrics(read_grayscale(args.image)).to_dict(), indent=2))


if __name__ == "__main__": main()
