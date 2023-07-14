import logging

from azure.functions import HttpRequest, HttpResponse


def main(req: HttpRequest) -> HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    content_type='application/json'
    

    # Set the appropriate content type for the response
    # content_type = 'image/jpeg'  # Modify based on your image file type

    # Return the image file as the response
    # return func.HttpResponse(body=json_object, status_code=200, mimetype=conten
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return HttpResponse(
            f"{req.get_json()}",
            status_code=200,
            mimetype=content_type
        )