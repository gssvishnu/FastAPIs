####################################
# @file		    - FastAPIs/settings.py
# @contributors - 
# @Usage	    - nil
# @Notes	    - Used to hold only FastAPI related global constants
####################################
import socket
import os 
import pathlib

''' Connections '''
host            = socket.gethostname()
port            = 8000

''' HTML '''
HTMLStaticDir   = os.path.join(pathlib.Path(__file__).parent.absolute(), "static")
print ("Serving {0} files from {1}".format(os.path.basename(HTMLStaticDir), HTMLStaticDir))
HTMLTemplateDir = os.path.join(pathlib.Path(__file__).parent.absolute(), "html_templates")
print ("Serving {0} files from {1}".format(os.path.basename(HTMLTemplateDir), HTMLTemplateDir))

CacheDir        = os.path.join(pathlib.Path(__file__).parent.absolute(), "cache")
print ("All Files will be stored to : {0}".format(CacheDir))

''' HTML Render Mapping '''
import fastapi.templating

templates = fastapi.templating.Jinja2Templates (
                                                directory="{0}".format(HTMLTemplateDir), extensions=['jinja2.ext.loopcontrols']
                                            )
                                            
HTMLRenderMapping = {
}

