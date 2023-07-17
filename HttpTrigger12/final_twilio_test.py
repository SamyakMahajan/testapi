import logging
import azure.functions as func
import json
# import json

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
    url_string = req.get_body()
    # Parse the URL-encoded string into a dictionary of parameters
    params = dict(param.split('=') for param in url_string.split('&'))

    # Retrieve the image URL from the parsed parameters
    image_url = params.get('MediaUrl0')

    # image_url=req.params.get('image_url')
    # logging.info('image_url: %s', image_url)

    # json_dict={
    #     'body': body,
         
    # }
    # json_object = json.dumps(json_dict, indent = 4) 
    # content_type='application/json'
   
# original_string = b'MediaContentType0=image%2Fjpeg&SmsMessageSid=MM34b3ee6de346ba069213c6be8404190e&NumMedia=1&ProfileName=Samyak+Mahajan&SmsSid=MM34b3ee6de346ba069213c6be8404190e&WaId=919013363029&SmsStatus=received&Body=Hu&To=whatsapp%3A%2B14155238886&NumSegments=1&ReferralNumMedia=0&MessageSid=MM34b3ee6de346ba069213c6be8404190e&AccountSid=ACcac64a7fd3d8c588ae857886acb0e122&From=whatsapp%3A%2B919013363029&MediaUrl0=https%3A%2F%2Fapi.twilio.com%2F2010-04-01%2FAccounts%2FACcac64a7fd3d8c588ae857886acb0e122%2FMessages%2FMM34b3ee6de346ba069213c6be8404190e%2FMedia%2FMEdcfc34442a7cdc21a926d06fbfc94b02&ApiVersion=2010-04-01'

# Decode from bytes to string
    # decoded_string = body.decode('utf-8')

# Parse the URL-encoded string
#     parsed_string = dict(param.split('=') for param in body.split('&'))

# # Convert the parsed string to a JSON object
#     json_data = json.dumps(parsed_string)
#     content_type='application/json'
    
    # return func.HttpResponse(body=json_data, status_code=200, mimetype=content_type)
    logging.info('image_url: %s', image_url)

    json_dict={
        'image_url': image_url
    }
    json_object = json.dumps(json_dict, indent = 4) 
    content_type='application/json'
    
    return func.HttpResponse(body=json_object, status_code=200, mimetype=content_type)
    

   