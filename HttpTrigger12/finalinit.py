import logging
import azure.functions as func




def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    image_url=req.params.get('image_url')
    logging.info('image_url: %s', image_url)
    
    return func.HttpResponse(
            f"hi {image_url} ",
            status_code=200
        )

   