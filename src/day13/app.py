# 플라스크 : 파이썬을 이용한 경량 웹 프레임워크
# 1. 플라스크 모듈 가져오기
from flask import Flask

# 2. 플라스크 객체 생성
app = Flask(__name__)

# 3. CORS허용 , 서로 다른 pot간의 통신 허용
from flask_cors import CORS
CORS(app)

from controller import *

# 3. 플라스크 웹 실행
if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug=True)
    # http://127.0.0.1:5000
    # http://localhost:5000
    # http://IP주소:5000
