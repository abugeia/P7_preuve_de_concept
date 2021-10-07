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
# Doesn't work : AttributeError: 'Conv' object has no attribute 'fuseforward'if the model exist
# ModuleNotFoundError: No module named 'utils.google_utils' if the model doesn't exist
if not(os.path.exists('model/modelYv3.pt')):
    modelYv3 = torch.hub.load('ultralytics/yolov3', 'yolov3_tiny', pretrained=True, force_reload=True)
    torch.save(modelYv3, 'model/modelYv3.pt')
else:
    modelYv3 = torch.load('model/modelYv3.pt')

##################################################
    # Gradio
##################################################

def yolo(im, size=640):
    '''Wrapper fn for gradio'''
    g = (size / max(im.size))  # gain
    im = im.resize((int(x * g) for x in im.size), Image.ANTIALIAS)  # resize

    results1 = modelYv3(im)  # inference
    results2 = modelYv5(im)  # inference
    results1.render()  # updates results.imgs with boxes and labels
    results2.render()  # updates results.imgs with boxes and labels
    return Image.fromarray(results1.imgs[0]), Image.fromarray(results2.imgs[0])

#----- Interface
# in1 = gr.inputs.Radio(['YOLOv3', 'YOLOv5'], label="Model", type='index')
in2 = gr.inputs.Image(type='pil', label="Original Image")
out1 = gr.outputs.Image(type="pil", label="YOLOv3")
out2 = gr.outputs.Image(type="pil", label="YOLOv5")


title = "YOLO"
description = "YOLO object detection. Upload an image or click an example image to use."
article = "Desciption (support html)"

examples = [['zidane.jpg'], ['bus.jpg']]
iface = gr.Interface(yolo, inputs=[in2], outputs=[out1, out2], title=title, description=description, article=article, examples=examples, analytics_enabled=False).launch(
    debug=True)

iface.launch()
