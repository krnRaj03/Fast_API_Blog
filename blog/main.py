from fastapi import FastAPI, Request
from . import  models
from . database import engine

#for html templates
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
from . routers import blog,user,authentication

#instantiating FastApi
app=FastAPI()

#Create Model
models.Base.metadata.create_all(engine)

#register Router
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)


#templates
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates1')))

@app.get("/paypal", response_class=HTMLResponse)
def paypal(request:Request):
  return templates.TemplateResponse("home.html", {'request':request})

@app.post("/api-m.sandbox.paypal.com/v1/oauth2/token")
def pp():
  pass
