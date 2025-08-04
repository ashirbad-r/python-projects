# Real-Time Object Detection with OpenCV and MobileNet SSD

This project uses a USB camera and the MobileNet SSD deep learning model to perform real-time object detection using OpenCV's `dnn` module.

## Model Information

The MobileNet SSD model used here is trained on the PASCAL VOC dataset. It supports detection of the following 20 object classes:

["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

## Project Structure

Object_detection_w_openCV/
├── MobileNetSSD_deploy.prototxt # Model architecture
├── MobileNetSSD_deploy.caffemodel # Pre-trained weights
├── usb_cam_object_detection.py # Main detection script
├── test_cam_gui.py # Webcam test script
└── README.md

## Requirements

- Python 3.6 or higher
- OpenCV with GUI support
- USB webcam

### Installation

Install the necessary Python packages:


## Download Model Files

wget -O MobileNetSSD_deploy.prototxt https://gist.githubusercontent.com/mm-aditya/797a3e7ee041ef88cd4d9e293eaacf9f/raw/MobileNetSSD_deploy.prototxt

wget -O MobileNetSSD_deploy.caffemodel https://sourceforge.net/projects/ip-cameras-for-vlc/files/MobileNetSSD_deploy.caffemodel/download
## Limitations

- Only 20 predefined object classes can be detected.
- For more object types (e.g., mobile phone, keyboard, mouse), consider switching to models trained on the COCO dataset (e.g., YOLOv5 or YOLOv8).

## References

- MobileNet SSD Model: https://github.com/chuanqi305/MobileNet-SSD
- OpenCV DNN Documentation: https://docs.opencv.org/master/d6/d0f/group__dnn.html
