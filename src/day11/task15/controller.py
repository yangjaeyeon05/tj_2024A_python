from app import app
from service import *
    # 4. app.run 코드 위에 HTTP 매핑 주소 정의 controller
@app.route("/qooqoo" , methods=['get']) # http://localhost:5000/qooqoo
def getqooqoo():
    # (1) 만약에 크롤링 된 csv 파일이 없거나 최신화하고 싶을때
    result = []
    qooqooStoreInfo(result);  # print(result)
    list2d_to_csv(result, '전국쿠우쿠우매장', ['번호', '지점명', '연락처', '주소', '영업시간'])
    # (2) csv에 저장된 정보 json으로 가져오기
    result2 = read_csv_to_json('전국쿠우쿠우매장')  # csv 파일을 json으로 가져오는 서비스 호출
    print(result2)
    # (3) 서비스로부터 받은 데이터로 HTTP 응답하기
    return result2