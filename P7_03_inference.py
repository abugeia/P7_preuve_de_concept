import gradio as gr
import torch
from PIL import Image
import os

##################################################
    # Modèle loading
##################################################

if not(os.path.isdir('model/')):
    os.system('mkdir model/')

#----- YOLOv5
if not(os.path.exists('model/modelYv5.pt')):
    modelYv5 = torch.hub.load('ultralytics/yolov5', 'yolov5s6', pretrained=True, force_reload=True)
    torch.save(modelYv5, 'model/modelYv5.pt')
else:
    modelYv5 = torch.load('model/modelYv5.pt')

#----- YOLOv3
if not(os.path.exists('model/modelYv3.pt')):
    modelYv3 = torch.hub.load('ultralytics/yolov3', 'yolov3_tiny', pretrained=True, force_reload=True)
    torch.save(modelYv3, 'model/modelYv3.pt')
else:
    modelYv3 = torch.load('model/modelYv3.pt')

##################################################
    # Gradio
##################################################
#------------ Wrapper
def yolo(size, iou, conf, im):
    '''Wrapper fn for gradio'''
    g = (int(size) / max(im.size))  # gain
    im = im.resize((int(x * g) for x in im.size), Image.ANTIALIAS)  # resize

    modelYv3.iou = iou
    modelYv5.iou = iou
    modelYv3.conf = conf
    modelYv5.conf = conf

    results1 = modelYv3(im)  # inference
    results2 = modelYv5(im)  # inference
    results1.render()  # updates results.imgs with boxes and labels
    results2.render()  # updates results.imgs with boxes and labels
    return Image.fromarray(results1.imgs[0]), Image.fromarray(results2.imgs[0])

#------------ Interface
in1 = gr.inputs.Radio(['640', '1280'], label="Taille d'image", default='1280', type='value')
in2 = gr.inputs.Slider(minimum=0, maximum=1, step=0.05, default=0.45, label='NMS IoU threshold')
in3 = gr.inputs.Slider(minimum=0, maximum=1, step=0.05, default=0.25, label='confidence threshold')
in4 = gr.inputs.Image(type='pil', label="Original Image")
out1 = gr.outputs.Image(type="pil", label="YOLOv3")
out2 = gr.outputs.Image(type="pil", label="YOLOv5")

title = "YOLO"
description = "YOLO object detection. Upload an image and click on submit."
article = "This page show the differences of inferences between YOLOv3 and YOLOv5"

examples = [['640',0.45, 0.25, 'img/zidane.jpg'], ['640',0.45, 0.25, 'img/bus.jpg']]
iface = gr.Interface(yolo, inputs=[in1, in2, in3, in4], outputs=[out1, out2], title=title, description=description, article=article, examples=examples, analytics_enabled=False).launch(
    debug=True)

iface.launch()
