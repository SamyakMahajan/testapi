import logging
import azure.functions as func
import os
import tempfile

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info("k1",req)
    # Check if the request has a file attached
    if not req.files or 'image' not in req.files:
        return func.HttpResponse(
            "Please attach an image file to the request.",
            status_code=400
        )

    # Access the image file from the request
    file = req.files['image']
    
    # Save the file to a temporary location
    temp_path = os.path.join(tempfile.gettempdir(), file.filename)
    file.save(temp_path)
###TODO: IS IT POSSIBLE TO DIRECTLY RETURN THE IMAGE FILE?
    # Read the image file contents
    with open(temp_path, 'rb') as image_file:
        image_data = image_file.read()

    # Set the appropriate content type for the response
    content_type = 'image/jpeg'  # Modify based on your image file type

    # Return the image file as the response
    return func.HttpResponse(body=image_data, status_code=200, mimetype=content_type)
