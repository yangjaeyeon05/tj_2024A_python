from flask import Flask
app = Flask(__name__)

# [모듈] controller.py의 매핑 함수들 가져오기
from controller import *

if __name__ == "__main__":
    app.run(debug=True)