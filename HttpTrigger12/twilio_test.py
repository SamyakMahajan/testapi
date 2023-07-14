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
    with open('image.jpg', 'rb') as image_file:
        image_data = image_file.read()

    # Set the content type and return the image as the response
    headers = {
        'Content-Type': 'image/jpeg'
    }

    return func.HttpResponse(body=image_data, headers=headers, status_code=200)
