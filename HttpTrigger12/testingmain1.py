from azure.functions import HttpRequest, HttpResponse
from azure.functions import func
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.get('/{name}')
async def get_name(name: str):
    return {'Welcome': f'{name}'}

@app.get("/api/{path}")
async def main(req: HttpRequest) -> HttpResponse:
    response = await app(req.scope, req.receive)
    return HttpResponse(
        response.body,
        status_code=response.status_code,
        headers=response.headers
    )
