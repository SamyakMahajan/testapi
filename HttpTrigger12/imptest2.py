import logging
# import tensorflow
import azure.functions as func
import json
from .predict import predict_image
import requests
from io import BytesIO
from  PIL import Image
import pandas as pd
import joblib
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # name = req.params.get('name')
    # image_url=req.params.get('image_url')
    # logging.info('image_url: %s', image_url)
    # image_data=predict_image(image_url)
    # model = joblib.load('classifier.pkl')
    # prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
#     if(prediction[0]>0.5):
#         prediction="Fake note"
#     else:
#         prediction="Its a Bank note"
#     return {
#         'prediction': prediction
#     }
    k=pd.read_csv("banknotes.py")
    variance=req.params.get('variance')
    skewness=req.params.get('skewness')
    curtosis=req.params.get('curtosis')
    entropy=req.params.get('entropy')

    

    # Return the image file as the response
    return func.HttpResponse(
            f"hi {curtosis} {variance} {entropy} {skewness}",
            status_code=200
        )

    # if image_url:
    #     return func.HttpResponse(f"Hello, {image_data}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #         "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #         status_code=200
    #     )
    # Set the appropriate content type for the response
    # content_type = 'image/jpeg'  # Modify based on your image file type

    # # Return the image file as the response
    # return func.HttpResponse(body=image_data, status_code=200, mimetype=content_type)

    # headers = {
    #     "Content-type": "application/json",
    #     "Access-Control-Allow-Origin":"*"
    # }
    # return func.HttpResponse(json.dumps(results), status_code=200,headers=headers)