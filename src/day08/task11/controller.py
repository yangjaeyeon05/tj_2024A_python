from app import app
from service import *
@app.route("/samsung" , methods = ["GET"])
def index():
    return samsungData()