# import requests
# from  PIL import Image
# # import json
# from io import BytesIO


def predict_image(image_url):
    # response = requests.get(image_url)
    # img = Image.open(BytesIO(response.content))
    tags=["shirt",'jacket',image_url] 
    return tags
# print(predict_image("https://blog.finxter.com/wp-content/uploads/2022/04/greenland_03a.jpg"))
