# day08 > task12 > service.py
f = open("아파트(매매)_실거래가_20240823.csv", 'r' , encoding='cp949')
data = []

while True:  # 안내문 부분 잘라내기
    line = f.readline().strip().strip("\"").split("\",\"")
    if line[0] == "NO":  # 데이터 제목 부분 : 안내문 마지막 부분까지 읽어서 버리고 루프 끝
        break
while True:  # 데이터 부분
    # 한 문장씩 읽고 / "\n" 제거 / 큰따옴표 제거 / 쉼표 단위로 나눠 리스트 형태로 line 변수명에 대입
    line = f.readline().strip().strip("\"").split("\",\"")
    if line == ['']:  # 공백이면 끝
        break
    # 데이터 CSV상 순서 (인덱스 찾기용)
    # "X","시군구","X","X","X","단지명","전용면적(㎡)","계약년월","계약일","거래금액(만원)[**금액1,금액2]","X","층","X","X","X","X","X","X","X","X"
    line[9] = "".join(line[9].split(','))
    data.append({"location": line[1], "name": line[5], "area": line[6], "year_month": line[7], "day": line[8],
            "contract_amount": line[9], "floor": line[11]})  # data 리스트에 line 추가
# print(data)

# 결과 데이터
# {'location': '인천광역시 서구 청라동', 'name': '호반베르디움앤영무예다음', 'area': '59.8600', 'year_month': '202308', 'day': '24', 'contract_amount': '44700', 'floor': '19'}
# [1] 인천광역시 아파트 실거래가의 모든 내역 정보 출력하시오.
def getall():
    return data

# [2] 가장 높은 거래금액 과 가장 낮은 거래금액의 해당 하는 거래의 시군구,단지명,전용면적 출력
def max_min_list():
    newList = []
    for dic in data:
        newList.append(int(dic['contract_amount']))
    print(max(newList))
    return

print(max_min_list())

# [4] 단지명 별로 거래량 계산해서 거래량이 많은 단지명 TOP10 출력
def top_ten_transaction():
    top_list = []  # 출력할 거래량 순위 목록
    complex_name = []  # 단지명 리스트

    return