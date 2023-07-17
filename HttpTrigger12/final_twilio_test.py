import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Parse the request body
    body = req.get_body().decode('utf-8')
    parsed_body = dict(param.split('=') for param in body.split('&'))

    # Extract the image URL from the parsed body
    image_url = parsed_body.get('MediaUrl0')

    # Create a JSON response with the image URL
    response_data = {
        'image_url': image_url
    }
    json_response = json.dumps(response_data)

    # Return the JSON response
    return func.HttpResponse(body=json_response, status_code=200, mimetype='application/json')
