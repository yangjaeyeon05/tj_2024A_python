from app import app
from service import *
    # 4. app.run 코드 위에 HTTP 매핑 주소 정의 controller
@app.route("/qooqoo" , methods=['get']) # http://localhost:5000/qooqoo
def getqooqoo():
    result = []

    return False