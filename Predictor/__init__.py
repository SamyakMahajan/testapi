import azure.functions as func

import logging

import json

import urllib.parse

import requests




def main(req: func.HttpRequest) -> func.HttpResponse:

   

#runni

    req_body = req.get_body().decode('utf-8')+"nooo"





   

    # parsed_string = urllib.parse.parse_qs(req_body)

   

    # json_data = dict(parsed_string)




    # final_data={}

    # for i in list(json_data):

    #     final_data[str(i)] = json_data[i]

   

    # return func.HttpResponse(f"{final_data['MediaUrl0'][0]}", status_code=200)

   






    return func.HttpResponse(f"{req_body}", status_code=200)