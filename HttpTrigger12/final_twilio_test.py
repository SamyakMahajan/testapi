import logging
import json
import azure.functions as func
# from urllib.parse import parse_qs
import urllib.parse

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Parse the request body as JSON
    req_body = req.get_body()
    #
    parsed_string = urllib.parse.parse_qs(req_body)

    json_data = dict(parsed_string)

    k=json_data["SmsMessageSid"]    
    return func.HttpResponse(f"{k}", status_code=200)
    
    # except:
    #      return func.HttpResponse("Not OK", status_code=400)

