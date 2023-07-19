import azure.functions as func
import logging
import json
import urllib.parse
import requests

import datetime
import os
import azure.functions as func
# from azure.cosmos import CosmosClient, PartitionKey

# Retrieve the Cosmos DB connection information from environment variables
# cosmosdb_uri = 'https://jb-expbuilder-d-cdb01.documents.azure.com:443/'
# cosmosdb_database = 'TagContainer'
# cosmosdb_container = 'kunal_db'

# def main(req: func.HttpRequest) -> func.HttpResponse:
    
#         # Get the request body
#         req_body = req.get_json()

#         # Extract the data from the request body
#         tags = req_body.get('tags')
#         # timestamp = datetime.datetime.utcnow().isoformat()
#         url = req_body.get('url')

#         # Connect to Azure Cosmos DB
#         client = CosmosClient(cosmosdb_uri, credential=None)
#         database = client.get_database_client(cosmosdb_database)
#         container = database.get_container_client(cosmosdb_container)

#         # Create a new item
#         item = {
#             'tags': ['jacket'],
#             # 'timestamp': timestamp,
#             'url': url
#         }

#         # Insert the item into the container
#         container.create_item(body=item, partition_key=PartitionKey(path='/tags'))

#         return func.HttpResponse("Data saved successfully.", status_code=200)

#     except Exception as e:
#         logging.error(f"An error occurred: {e}")
#         return func.HttpResponse("Error occurred while saving data.", status_code=500)






def main(req: func.HttpRequest) -> func.HttpResponse:
    
#runni
    req_body = req.get_body().decode('utf-8')

    # req_json=json.loads(req_body)
    # url=req_json['name']


    # parsed_string = urllib.parse.parse_qs(req_body)
    # json_data = dict(parsed_string)

    # json_data = dict(parsed_string)

    # s=""

    # final_data={}

    # for i in list(json_data):

    #     final_data[str(i)] = json_data[i]
    # url=json_data["name"]
    # Connect to Azure Cosmos DB
    # client = CosmosClient(cosmosdb_uri, credential=None)
    # database = client.get_database_client(cosmosdb_database)
    # container = database.get_container_client(cosmosdb_container)

    # # Create a new item
    # item = {
    #     'tags': ['jacket'],
    #     # 'timestamp': timestamp,
    #     'url': url
    # }

    # # Insert the item into the container
    # container.create_item(body=item, partition_key=PartitionKey(path='/tags'))

    # parsed_string = urllib.parse.parse_qs(req_body)
    
    # json_data = dict(parsed_string)

    # final_data={}
    # for i in list(json_data):
    #     final_data[str(i)] = json_data[i]
    
    # return func.HttpResponse(f"{final_data['MediaUrl0'][0]}", status_code=200)
    



    return func.HttpResponse(f"{req_body}", status_code=200)