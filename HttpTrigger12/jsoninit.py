import logging
# import tensorflow
import azure.functions as func
import json



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    a=2
    b=3
    c=a+b
    name = req.params.get('name')
    a=int(req.params.get('a'))
    b=int(req.params.get('b'))
    c=a+b
    d={
        'a': a,
        'b': b,
        'a+b': c,
    }
    json_object = json.dumps(d, indent = 4) 
    content_type='application/json'
    

    # Set the appropriate content type for the response
    # content_type = 'image/jpeg'  # Modify based on your image file type

    # Return the image file as the response
    return func.HttpResponse(body=json_object, status_code=200, mimetype=content_type)
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          f"The sum of {a} and {b} is {c}",
    #          status_code=200
    #     )




# def iosum(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')
    
#     # a=2
#     # b=3
#     # c=a+b
#     name = req.params.get('name')
#     a=int(req.params.get('a'))
#     b=int(req.params.get('b'))
#     c=a+b
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              f"The sum of {a} and {b} is {c}",
#              status_code=200
#         )