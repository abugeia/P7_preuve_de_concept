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

<img src="https://github.com/abugeia/7_preuve_de_concept/blob/master/img/P7_02_eval_coco.png" width="400px"/>

```bash
python P7_02_eval_coco.py
```
Application pour comparer les résultats d'inférence entre les deux algorithmes en mAP et en temps de calcul.

<img src="https://github.com/abugeia/7_preuve_de_concept/blob/master/img/P7_03_inference.png" width="400px"/>

```bash
python P7_03_inference.py
```
L'application est ensuite visible dans un navigateur à l'adresse http://127.0.0.1:7860/  

Entrainement de YOLO sur le dataset OpenImage  
Notebook : P7_04_yolov5_train_eval_OpenImages.ipynb

<img src="https://github.com/abugeia/7_preuve_de_concept/blob/master/img/P7_04_yolov5_train_eval_OIds.png" width="400px"/>

## References

COCO dataset    :   [https://cocodataset.org/#home](https://cocodataset.org/#home)  
YOLOv5 Githu    :   [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)  
OIDv6 Github    :   [https://github.com/NanoCode012/OIDv6_ToolKit_Download_Open_Images_Support_Yolo_Format](https://github.com/NanoCode012/OIDv6_ToolKit_Download_Open_Images_Support_Yolo_Format)

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
