# P7 Détection d'objets avec YOLO

Ce projet permet :
    1. d'évaluer le split validation du dataset COCO avec YOLOv3 et YOLOv5.
    2. de comparer les résultats d'inférence sur une image traitée avec chaque algorithme

## Installation

```bash
pip install -r requirements.txt
```

## Notice

Evaluation du split validation du dataset COCO avec YOLOv3 et YOLOv5

```bash
python P7_02_eval_coco.py
```
Application pour comparer les résultats d'inférence entre les deux algorithmes

```bash
python P7_02_inference.py
```
L'application est ensuite visible dans un navigateur à l'adresse http://127.0.0.1:7860/

## References

COCO dataset :     [https://cocodataset.org/#home](https://cocodataset.org/#home)
YOLOv5 Github     [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)

## Results

Inference
<img src="./img/inference.png" width="600px"/>