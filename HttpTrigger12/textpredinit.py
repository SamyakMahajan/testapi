import logging
# import tensorflow
import azure.functions as func

# from azure.functions import HttpRequest, HttpResponse
# from azure.functions import func

import numpy as np
import pandas as pd
# import pandas as pd

# from BankNotes import BankNote
# app = FastAPI()



# @app.get("/")
# def index():
#     return {"message": "Hello World"}

# @app.get('/{name}')
# def get_name(name: str):
#     return {'Welcome ': f'{name}'}

# @app.post('/predict')
# def predict_banknote(variance,skewness,curtosis,entropy):
#     # data=data.model_dump()
#     # variance=data['variance']
#     # skewness=data['skewness']
#     # curtosis=data['curtosis']
#     # entropy=data['entropy']
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
# @app.get("/")
# async def main(req: HttpRequest) -> HttpResponse:
#     # Pass the Azure Functions request to the FastAPI application
#     # and get the FastAPI response
#     response = await app(req.scope, req.receive)
    
#     # Create and return the Azure Functions response
#     return HttpResponse(
#         response.body,
#         status_code=response.status_code,
#         headers=response.headers
#     )



classifier = {}

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        n=np.array([1,2,3])
        # logging.info('Python HTTP trigger function processed a request.')
        # classifier['model'] = joblib.load('mymodel.pkl')
        k=pd.DataFrame(n)
        return func.HttpResponse(f"Hello, It was succesfull, n = {n}")
    except:    
    # # pickle_in=open('classifier.pkl','rb')
    # classifier=pickle.load(model)
        name = req.params.get('name')
        a=int(req.params.get('a'))
        b=int(req.params.get('b'))
        c=a+b
        if not name:
            try:
                req_body = req.get_json()
            except ValueError:
                pass
            else:
                name = req_body.get('name')

        if name:
            return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
        else:
            return func.HttpResponse(
                f"The sum of {a} and {b} is {c}",
                status_code=200
            )



