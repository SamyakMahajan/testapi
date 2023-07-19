import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        # Assuming the JSON request contains a 'message' field
        message = req_body.get('name')

        # Process the message
        # processed_message = process_message(message)

        response = {'result': message}
        return func.HttpResponse(json.dumps(response), mimetype='application/json')
    
    except ValueError as e:
        logging.error(e)
        return func.HttpResponse('Invalid JSON', status_code=400)
