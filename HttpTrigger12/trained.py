import requests

from  PIL import Image

from io import BytesIO

from ultralytics import YOLO

import matplotlib.pyplot  as plt




model = YOLO('yolov8n.yaml')             # location of model pt file

names = model.names

tolerance_level = 0.50




def predict_image(image_url):

    response = requests.get(image_url)

   

    results=model.predict(source=response, conf=0.4, save=False, line_width=2)

    ans =[]

    for r in results:

        for i in range(len(r.boxes.cls)):

            if round(float(r.boxes.conf[i]), 3) >=  tolerance_level :

                ans.append(names[int(r.boxes.cls[i])])

    return ans