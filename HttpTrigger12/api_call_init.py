import logging
import json
import azure.functions as func
# from urllib.parse import parse_qs
import urllib.parse
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Parse the request body as JSON
    req_body = req.get_body().decode('utf-8')
    #
    ##decoded_string = original_string.decode('utf-8')

    parsed_string = urllib.parse.parse_qs(req_body)

    json_data = dict(parsed_string)
    # json_data = dict(parsed_string)
    # s=""
    final_data={}
    for i in list(json_data):
        final_data[str(i)] = json_data[i]
        # s+=" "
    if(int(final_data['NumMedia'][0])==0):
        return func.HttpResponse(f"Please upload a picture", status_code=200)
    # print(s)'
    # a=requests.post("https://jb-eb-d-functionapp001.azurewebsites.net/api/Predictor?code=3Lj3drbXQVpO3bPSSDyMRX_PNxD5UXir02JYkyO1TA09AzFubN7qMw==")
    # a=a.content.decode('utf-8')
    # k=json_data["SmsMessageSid"]    
    # k={"name":str(final_data['MediaUrl0'])}
    # url="https://jb-eb-d-functionapp001.azurewebsites.net/api/Predictor?code=3Lj3drbXQVpO3bPSSDyMRX_PNxD5UXir02JYkyO1TA09AzFubN7qMw=="
    # json_object = json.dumps(k, indent = 4)
    # headers = {'Content-type': 'application/json'}
    # response = requests.post(url, data=json_object, headers=headers)d
    # response=response.content.decode('utf-8')
    else:
        media_url=final_data['MediaUrl0'][0]
        return func.HttpResponse(f"{final_data['MediaUrl0'][0]} : {type(media_url)}", status_code=200)
    
    # except:
    #      return func.HttpResponse("Not OK", status_code=400)
