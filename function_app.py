import azure.functions as func
import datetime
import json
import logging
import csv 
import codecs
from addition_function import bp

app = func.FunctionApp()

app.register_blueprint(bp)

@app.function_name("FirstHTTPFunction")
@app.route(route="myroute",auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest)->func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    return func.HttpResponse(
        "Wow this HTTP function Works!!!",
        status_code=200
    )

@app.function_name("SecondHTTPFunction")
@app.route(route="newroute")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Starting the second HTTP Function request.")
    name = req.params.get('name')
    if name:
        message=f"Hello, {name}, so glad this Function worked!!"
    else:
        message="Hello, so glad this Function worked!!"
    return func.HttpResponse(
        message,
        status_code=200
    )



# @app.function_name(name="MyFirstBlobFunction")
# @app.blob_trigger(arg_name="myblob",
#                   path="newcontainer/youtube_analysis.ipynb",
#                   connection="AzureWebJobsStorage")
# def test_function(myblob: func.InputStream):
#     logging.info(f"Python blob function trigger after the youtube_analysis.ipynb was uploaded to new container. So cool!!!"
#                  f"Printin the name of the blob path: {myblob.name}"
#                  )
    
# @app.function_name(name="ReadFileBlobFunction")
# @app.blob_trigger(arg_name="readfile",
#                   path="newcontainer/Churn_Modelling.csv",
#                   connection="AzureWebJobsStorage")
# def main(readfile: func.InputStream):
#     reader=csv.reader(codecs.iterdecode(readfile,'utf-8'))
#     for line in reader:
#         print(line)