####################################
# @file		    - FastAPIs/main.py
# @contributors - 
# @Usage	    - python3 main.py
# @Notes	    - Main function to serve as entry point for all APIs 
#                 which are imported and called up.
####################################
# Imports
import uvicorn
from typing import Union
import os
import ssl
import sys
import json
from inspect import iscoroutinefunction

#FAST APIs 
import fastapi
from starlette.middleware.cors import CORSMiddleware 
import fastapi.responses
from fastapi.staticfiles import StaticFiles
# Security Related
import fastapi.security
import base64
import requests
import socket

# local imports
import settings
sys.path.append("python_modules")
import newCaseTemplate
import caseCategory
import caseOperations

# Global Variables to be used for FAST APIs 
app         = fastapi.FastAPI()

''' Make FastAPI as HTTPS '''
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('./ssl_keys/cert.pem', keyfile='./ssl_keys/key.pem')

''' CORS '''
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
''' END of CORS '''

''' HTML Rendering Templates '''
app.mount(
    "/{0}".format(os.path.basename(settings.HTMLStaticDir)),
    StaticFiles(directory=settings.HTMLStaticDir),
    name="{0}".format(os.path.basename(settings.HTMLStaticDir)),
)

#--------- Security Module -----------------#
security = fastapi.security.HTTPBasic()
def get_current_username (credentials: fastapi.security.HTTPBasicCredentials = fastapi.Depends(security)):
    with requests.session() as s:
        userAndPass = base64.b64encode(bytes(f"{credentials.username}:{credentials.password}", encoding='utf-8')).decode("ascii")
        headers = {'Authorization' : f'Basic {userAndPass}'}
        if credentials.username != "admin":
            raise fastapi.HTTPException(
                status_code = fastapi.status.HTTP_401_UNAUTHORIZED, 
                detail="Incorrect username / password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return credentials.username
    
@app.get("/authenticate")    
def read_current_user (username: str=fastapi.Depends(get_current_username)):
    if type(username) != str:
        raise fastapi.HTTPException(
            status_code = fastapi.status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect username / password",
            headers={"WWW-Authenticate": "Basic"},
        )
    else:
        return username
        
@app.get("/logout")    
def LogOut (username: str=fastapi.Depends(get_current_username)):
    raise fastapi.HTTPException(
            status_code = fastapi.status.HTTP_401_UNAUTHORIZED , 
            detail="Logged out from Application..!! Re - open Home page for Login."
        )
        
@app.get("/", response_class=fastapi.responses.HTMLResponse)
def newcase(request: fastapi.Request, username: str=fastapi.Depends(read_current_user)):
    context = {"request": request}
    context['User'] = username
    context['JSONData'] = caseOperations.GetAllCases()
    return settings.templates.TemplateResponse("dashboard.html", context)
    
@app.get("/viewcase", response_class=fastapi.responses.HTMLResponse)
def viewcase(request: fastapi.Request, cta: Union[str, None]=None, username: str=fastapi.Depends(read_current_user)):
    context = {"request": request, "cta" : cta}
    context['User'] = username
    context['JSONData'] = caseOperations.viewcase(cta)
    return settings.templates.TemplateResponse("viewcase.html", context)

@app.get("/newcase", response_class=fastapi.responses.HTMLResponse)
def newcase(request: fastapi.Request):
    context = {"request": request}
    return settings.templates.TemplateResponse("newcase.html", context)
    
@app.post("/GetVerdict")
def GetVerdict(newCaseObj:newCaseTemplate.newCase):
    ReturnJSON = {}
    ReturnJSON["verdict"], ReturnJSON["IsAffidavit"], ReturnJSON["AffidavitType"] = caseCategory.main(newCaseObj)
    return ReturnJSON

@app.post("/SubmitCase")
def SubmitCase(newCaseObj:newCaseTemplate.SubmitCase):
    return caseOperations.SubmitNewCase(newCaseObj)
    
# Main function
# Removes depdendency to run lengthy command, so that we can run python3 __file__.py
# Else we should run python3 -m uvicorn main:app --reload --host $HOSTNAME --port 8000
def main ():
    print ("Access the APIs at http://{0}:{1}/docs".format(host, port))
    uvicorn.run(app, host=host, port=port)
    
if __name__ == "__main__":
    main ()
