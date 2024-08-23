# day08 > task12 > controller.py
from app import app
import service

@app.route("/getall" , methods = ["GET"])
def getall():
    return service.getall()

@app.route("/maxminlist" ,methods = ["GET"])
def maxminlist():
    return service.max_min_list()