import torch
import os
from sys import platform
import sys, subprocess

if platform == "linux" or platform == "linux2":
    syst = 0
elif platform == "darwin":
    # OS X
    syst = 1
elif platform == "win32":
    syst = 1
##################################################
    # Dataset
##################################################

def test_if_exist_ds():
    url_folder = 'https://github.com/ultralytics/yolov5/releases/download/v1.0/'
    val_file = 'coco2017val.zip'

    if not(os.path.isdir('datasets/coco/')):
        # Download COCO val2017
        torch.hub.download_url_to_file(url_folder + val_file, 'tmp.zip')
        if syst == 0:
            os.system('unzip -q tmp.zip -d ./datasets && rm tmp.zip')
        elif syst == 1:
            print('you must extract the tmp.zip in /datasets and relaunch the app')
            sys.exit()

test_if_exist_ds()
##################################################
    # Load YOLO v3 & v5
##################################################

print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)


## Load and test the model with eval file
os.system('git clone https://github.com/ultralytics/yolov5')  # clone repo
# os.system('cd yolov5/')
os.chdir("yolov5")
os.system('pip install -qr requirements.txt')
# os.system('cd ..')
os.chdir(dname)
# clone repo
os.system('git clone https://github.com/ultralytics/yolov3')

# os.system('cd /yolov3/')
os.chdir("yolov3")
# install dependencies
os.system('pip install -qr requirements.txt')
# os.system('cd ..')
os.chdir(dname)

##################################################
    # Testing YOLO v3 & v5
##################################################

#----------------- YOLOv5 -----------------
os.chdir("yolov5")
import subprocess

print("-"*50)
if torch.cuda.is_available():
    print('Evaluation of YOLOv5(m6) on COCO validation set with gpu')
    print("-"*50)
    subprocess.call(['python', 'val.py', '--weights', 'yolov5m6.pt', '--data', 'data/coco.yaml', '--img', '1280', '--iou', '0.65', '--half'])
else:
    print('Evaluation of YOLOv5(s) on COCO validation set with cpu')
    print("-"*50)
    subprocess.call(['python', 'val.py', '--weights', 'yolov5m6.pt', '--data', 'data/coco.yaml', '--img', '1280', '--iou', '0.65'])
os.chdir(dname)

#----------------- YOLOv3 -----------------
if syst == 0:
    os.system('mv ./datasets/coco ./')
elif syst == 1:
    os.system('move ./datasets/coco ./')
os.chdir("yolov3")
print("-"*50)
print('Evaluation of YOLOv3 on COCO validation set with cpu')
print("-"*50)
subprocess.call(['python', 'test.py', '--weights', 'yolov3.pt', '--data', 'data/coco.yaml', '--img', '640', '--iou', '0.65'])
os.chdir(dname)

# #----------------- YOLOv5 -----------------
# # os.system('cd yolov5/')
# os.chdir("yolov5")
# # Run YOLOv5x on COCO val2017
# if torch.cuda.is_available():
#     print('Eval with gpu')
#     os.system('python val.py --weights yolov5s.pt --data data/coco.yaml --img 640 --iou 0.65 --half')
# else:
#     print('Eval with cpu')
#     os.system("python val.py --weights yolov5s.pt --data data/coco.yaml --img 640 --iou 0.65")
# # os.system('cd ..')
# os.chdir(dname)
# 
# 
# #----------------- YOLOv3 -----------------
# if syst == 0:
#     os.system('mv ./datasets/coco ./')
# elif syst == 1:
#     os.system('move ./datasets/coco ./')
# # os.system('cd yolov3/')
# os.chdir("yolov3")
# os.system('python test.py --weights yolov3.pt --data data/coco.yaml --img 640 --iou 0.65')

# # os.system('cd ..')
# os.chdir(dname)


# # put back ds in datasets/ folder
if syst == 0:
    os.system('mv ./coco ./datasets/')
elif syst == 1:
    os.system('move ./coco ./datasets/')