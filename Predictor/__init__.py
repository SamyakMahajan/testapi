import logging
import azure.functions as func
import json
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()

    final_data = {}
    for key, value in req_body.items():
        final_data[key] = value

    return func.HttpResponse(json.dumps(final_data), mimetype='application/json')
