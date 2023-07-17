import logging
import azure.functions as func
import json
# from .finalpredict import predict_image #this imports the prediction function
# from .predict import predict_image

"""
    what we will do:
    1. give image url from azure storage to the API request
    2. pass the URL to the predict function and return the tags 
    3. return the tags in JSON format
"""


"""
    Tasks done:
    1. Can Accept image_url as a request parameter and succesfuly return an OK response
    2. Returns output as JSON type
"""

"""
    Tasks todo:
    ultralytics library needs torch as a dependency but since it is a big size, we need to add torch using blob, ONNX file or as a dependency folder directly instead: currently trying out ONNX
"""


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    #functionname/myconfig.json
    body=req.get_body()
    # image_url=req.params.get('image_url')
    # logging.info('image_url: %s', image_url)

    json_dict={
        'body': body,
         
    }
    json_object = json.dumps(json_dict, indent = 4) 
    content_type='application/json'
    
    return func.HttpResponse(body=json_object, status_code=200, mimetype=content_type)
    

   