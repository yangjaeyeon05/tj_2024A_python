'''
    삼성전자주가.csv 파일의 정보를 테이블 형식으로 localhost:8080/index3.html으로 출력
        1. csv 파일을 읽어서 한줄씩 딕셔너리로 변환 후 리스트에 담기
        2. 플라스크 이용한 HTTP 매핑 정의하기
        3. 스프링서버에서 AJAX를 이용한 플라스크 서버로
'''

from flask import Flask # (1) Flask 모듈 가져오기
app = Flask(__name__)   # (2) Flask 객체 생성

from flask_cors import CORS # (3) CORS 모듈 가져오기 # CORS : 교차 출처 자원 공유 허용
CORS(app)   # (4) 모든 HTTP 경로의 CORS 허용
# (5) 매핑 , controller 호출
from controller import *

if __name__ == "__main__":  # (6) Flask 실행
    app.run(debug=True)