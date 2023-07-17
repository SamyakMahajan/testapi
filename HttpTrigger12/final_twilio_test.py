import logging
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Parse the request body as JSON
    req_body = req.get_json()

    # Check if the message contains media (image)
    if 'NumMedia' in req_body and int(req_body['NumMedia']) > 0:
        # Extract the image URL
        media_url = req_body['MediaUrl0']
        # Do something with the image URL, such as storing it or processing it further
        logging.info(f"Received image URL: {media_url}")

    return func.HttpResponse("OK", status_code=200)

