import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_body().decode('utf-8')

    return func.HttpResponse(f"{req_body}", status_code=200)