import logging
import azure.functions as func

"""
    Tasks done:
    1. Can Accept image_url as a request parameter and succesfuly return an OK response
"""

"""
    Tasks todo:
    ultralytics library needs torch as a dependency but since it is a big size, we need to add torch using blob or as a dependency folder directly instead 
"""


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    image_url=req.params.get('image_url')
    logging.info('image_url: %s', image_url)
    
    return func.HttpResponse(
            f"hi the image was recieved. Its URL is: {image_url} ",
            status_code=200
        )

   