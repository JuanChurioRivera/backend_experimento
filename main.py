from fastapi import FastAPI,Request
from azureSQL import connect_api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins= '*',  # 
    allow_methods=["GET", "POST"],  # Only allow methods you use
    allow_headers=["Authorization", "Content-Type"],  # Only allow headers you use
)

app.include_router(connect_api.router)

@app.api_route('/', methods=['GET', 'HEAD','POST'])



async def root(request:Request):# request asyncronic
    if request.method == 'POST':
        print('porfi')
    return "¡Hola Api!"