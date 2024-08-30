from app import app
from service import *
    # 4. app.run 코드 위에 HTTP 매핑 주소 정의 controller
@app.route("/total" , methods=['get']) # http://localhost:5000/qooqoo
def getTotal():
    result = total()
    print(result)
    return result

@app.route("/area" , methods=['get']) # http://localhost:5000/qooqoo
def getArea():
    result = area()
    print(result)
    return result

@app.route("/noduplication" , methods=['get']) # http://localhost:5000/qooqoo
def noduplication():
    result = no_duplication()
    print(result)
    return result

@app.route("/highesttrading" , methods=['get']) # http://localhost:5000/qooqoo
def highesttrading():
    result = highest_trading()
    print(result)
    return result

@app.route("/trans" , methods = ['get'])
def trans():
    return total1()
