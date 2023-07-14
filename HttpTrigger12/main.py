import uvicorn
from fastapi import FastAPI
from azure.functions import HttpRequest, HttpResponse
from azure.functions import func

import numpy as np
# import pickle
import pandas as pd

from .banknotes import BankNote
app = FastAPI()

# pickle_in=open('classifier.pkl','rb')
# classifier=pickle.load(pickle_in)

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get('/{name}')
def get_name(name: str):
    return {'Welcome ': f'{name}'}

# @app.post('/predict')
# def predict_banknote(data:BankNote):
#     data=data.model_dump()
#     variance=data['variance']
#     skewness=data['skewness']
#     curtosis=data['curtosis']
#     entropy=data['entropy']
#     prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
#     if(prediction[0]>0.5):
#         prediction="Fake note"
#     else:
#         prediction="Its a Bank note"
#     return {
#         'prediction': prediction
#     }

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.1.1', port=7000)

# Create an instance of your FastAPI application
# app = FastAPI()

# Define an Azure Functions HTTP trigger function
@app.get("/")
async def main(req: HttpRequest) -> HttpResponse:
    # Pass the Azure Functions request to the FastAPI application
    # and get the FastAPI response
    response = await app(req.scope, req.receive)
    
    # Create and return the Azure Functions response
    return HttpResponse(
        response.body,
        status_code=response.status_code,
        headers=response.headers
    )




