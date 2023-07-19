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
    # print(s)
    # k=json_data["SmsMessageSid"]   
    # 

    # The code for posting on other azure function
    media_url=final_data['MediaUrl0'][0]
    func_url="https://fashion-ml-02.azurewebsites.net/api/tag_prediction_func?code=u3X7XkaTiTnE3GRKr0SrNyvSmo48a-YyZRr-8z0fDGieAzFuY8Vu7g=="
#just for commiting
    
    k={"name":media_url}
    url=func_url
    json_object = json.dumps(k, indent = 4)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=json_object, headers=headers)
    response=response.content.decode('utf-8')
    #the code ends for posting on other azure function


    return func.HttpResponse(f"{response}", status_code=200)
    
    # except:
    #      return func.HttpResponse("Not OK", status_code=400)
