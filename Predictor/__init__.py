import logging
import json
import azure.functions as func
import urllib.parse


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_body().decode('utf-8')
    parsed_string = urllib.parse.parse_qs(req_body)

    json_data = dict(parsed_string)
    # json_data = dict(parsed_string)
    # s=""
    final_data={}
    for i in list(json_data):
        final_data[str(i)] = json_data[i]
    final=final_data['name']
    return func.HttpResponse(f"{final}", status_code=200)