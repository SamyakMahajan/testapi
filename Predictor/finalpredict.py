from ultralytics import YOLO
import matplotlib.pyplot  as plt

"""
    This module implements the predict_image function which takes in an image URL 
    and returns a list of tags recognised in the image
"""


def predict_image(image_url):
    
    model = YOLO('yolov8n.yaml')             # location of model pt file
    names = model.names
    tolerance_level = 0.50
    results=model.predict(source=image_url, conf=0.4, save=False, line_width=2)
    ans =[]
    for r in results:

        for i in range(len(r.boxes.cls)):

            if round(float(r.boxes.conf[i]), 3) >=  tolerance_level :

                ans.append(names[int(r.boxes.cls[i])])

    return ans