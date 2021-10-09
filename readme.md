# P7 Détection d'objets avec YOLO

Ce projet permet :  
    * d'évaluer le split validation du dataset COCO avec YOLOv3 et YOLOv5.  
    * de comparer les résultats d'inférence sur une image traitée avec chaque algorithme
    * D'entraîner un modèle YOLOv5 sur une extraction du dataset Open Image

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

Entrainement de YOLO sur le dataset OpenImage
Notebook : P7_04_yolov5_train_eval_OpenImages.ipynb

## References

COCO dataset :     [https://cocodataset.org/#home](https://cocodataset.org/#home)  
YOLOv5 Github:     [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)

## Results

### Inference  
<img src="https://github.com/abugeia/7_preuve_de_concept/blob/master/img/inference.PNG" width="600px"/>

### Evaluation  
YOLOv3  
<img src="https://github.com/abugeia/7_preuve_de_concept/blob/master/img/yolov3_results.PNG" width="400px"/>

YOLOv5  
<img src="https://github.com/abugeia/7_preuve_de_concept/blob/master/img/yolov5_results.PNG" width="400px"/>

### Trained YOLO on OpenImage dataset
<img src="https://github.com/abugeia/7_preuve_de_concept/blob/master/img/inference_trained_yolo.PNG" width="800px"/>
