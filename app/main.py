
from fastapi import FastAPI
from routers.inference import router as inference_routes
import os

app = FastAPI()


def start_app():
    ''' Initialises and configures application 
        including routes and api settings.
    '''
    app.include_router(inference_routes)
    print("App initialised!!")


start_app()
