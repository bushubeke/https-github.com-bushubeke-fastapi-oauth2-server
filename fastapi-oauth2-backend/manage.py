import typer
import asyncio
import uvicorn
import subprocess
from pathlib import Path


SOURCE_FILE = Path(__file__).resolve()
SOURCE_DIR = SOURCE_FILE.parent

# from fastapi_migrations import MigrationsConfig, Migrations
# from fastapi_migrations.cli import MigrationsCli
# print(SOURCE_DIR)
# from fastapi_sqlalchemy import DBSessionMiddleware
from oauth2.main import create_dev_app
from oauth2.config import settings
from oauth2.models import async_main,droptables


capp = typer.Typer()
app=create_dev_app()


@capp.command()
def upgrade(version):
    asyncio.run(async_main())
    
@capp.command()
def test():
    subprocess.run(["pytest", "-v"])
@capp.command()
def run():
    subprocess.run(["uvicorn", "manage:app", "--host" ,"0.0.0.0","--port","7000","--reload"])
 
@capp.command()
def rung():
   
    subprocess.run(["gunicorn", "manage:app", "-k" ,"uvicorn.workers.UvicornWorker","-b" ,"0.0.0.0:9000","--reload","-w","1"]) 
@capp.command()
def drop():
    asyncio.run(droptables())

if __name__ == "__main__":
    capp()