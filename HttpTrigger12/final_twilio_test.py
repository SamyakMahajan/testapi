import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Parse the request body as JSON
    req_body = req.get_json()
    # try:
    # # Check if the message contains media (image)
    #     if 'NumMedia' in req_body and int(req_body['NumMedia']) > 0:
    #         # Extract the image URL
    #         media_url = req_body['MediaUrl0']
    #         # Do something with the image URL, such as storing it or processing it further
    #         logging.info(f"Received image URL: {media_url}")

    return func.HttpResponse("OK", status_code=200)
    
    # except:
    #      return func.HttpResponse("Not OK", status_code=400)

