import azure.functions as func
import urllib.request

def main(req: func.HttpRequest) -> func.HttpResponse:
    # URL-encoded string containing the image URL
    url_string = req.get_body()
    # Parse the URL-encoded string into a dictionary of parameters
    params = dict(param.split('=') for param in url_string.split('&'))

    # Retrieve the image URL from the parsed parameters
    image_url = params.get('MediaUrl0')

    # Download the image using urllib
    urllib.request.urlretrieve(image_url, 'image.jpg')

    # Open the image file
    #  if not req.files or 'image' not in req.files:
    #     return func.HttpResponse(
    #         "Please attach an image file to the request.",
    #         status_code=400
    #     )
    with open('image.jpg', 'rb') as image_file:
        image_data = image_file.read()
    # Access the image file from the request
    # file = req.files['image']


#     # Save the file to a temporary location
#     temp_path = os.path.join(tempfile.gettempdir(), file.filename)
#     file.save(temp_path)
# ###TODO: IS IT POSSIBLE TO DIRECTLY RETURN THE IMAGE FILE?
#     # Read the image file contents
    
#     # Set the appropriate content type for the response
#     content_type = 'image/jpeg'  # Modify based on your image file type

#     # Return the image file as the response
#     return func.HttpResponse(body=image_data, status_code=200, mimetype=content_type)
    

    # Set the content type and return the image as the response
    headers = {
        'Content-Type': 'image/jpeg'
    }

    return func.HttpResponse(body=image_data, headers=headers, status_code=200)
