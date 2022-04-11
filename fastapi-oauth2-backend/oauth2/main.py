
from fastapi import FastAPI,Header
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from .models import asyncengine
# from .models.dbconnect import async_session,engine
from .models import Role,RoleModel,User,UserModel

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_dev_app():
    app=FastAPI()
   
    
    origins = [ "*"]
    app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            )

    
    templates = Jinja2Templates(directory="templates")
    app.mount("/static", StaticFiles(directory="oauth2/static"), name="static")
    
    @app.get("/")
    def index(x_app_key: Optional[str] = Header(None) ,x_refresh_key: Optional[str] =Header(None)):
        return {"Message":"You should make your own index page"}
    
    return app


def create_prod_app():
    app=FastAPI()
    
    app.mount("/static", StaticFiles(directory="/app/static"), name="static")    
    
    
    
    #############################################################3
    # heroku settings 
    #  https://fastapi-oauth2.herokuapp.com/
    #  https://git.heroku.com/fastapi-oauth2.git

    # web: gunicorn manage:app -k uvicorn.workers.UvicornWorker -b 0.0.0.0:9000 --reload -w 2
    # web: gunicorn -b 0.0.0.0:9000 --reload -w 4 -k uvicorn.workers.UvicornWorker manage:app
    
    
    ##############################################################