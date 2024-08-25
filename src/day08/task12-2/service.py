f = open("아파트(매매)_실거래가_20240823.csv", 'r' , encoding='cp949')
list = []
data = f.read() # 파일 읽기
# print(data)
rows = data.split("\n") # 행구분
# print(rows)
rowsSize = len(rows)-1  # 마지막 인덱스 제외
# print(rowsSize)
for row in rows[16:rowsSize]:   # 데이터 중 앞 부분 없애야 하는 부분이 많아서 16 인덱스부터 시작
    cols = row.strip("\"").split("\",\"")  # 데이터에 ,(쉼표)가 많이 들어가서 split 기준을 ","으로 잡아서 자르기
    # print(cols)
    dic = {
        'location' : cols[1] ,
        'name' : cols[5] ,
        'area' : cols[6] ,
        'year_month' : cols[7] ,
        'day' : cols[8] ,
        'contract_amount' : cols[9] ,
        'floor' : cols[11]
    }
    list.append(dic)
#print(list)
# 결과 데이터
# {'location': '인천광역시 서구 청라동', 'name': '호반베르디움앤영무예다음', 'area': '59.8600', 'year_month': '202308', 'day': '24', 'contract_amount': '44700', 'floor': '19'}
# [1] 인천광역시 아파트 실거래가의 모든 내역 정보 출력하시오.
def getall():
    return list

# [2] 가장 높은 거래금액 과 가장 낮은 거래금액의 해당 하는 거래의 시군구,단지명,전용면적 출력
def max_min_list():
    contract_amountList = []
    for dic in list:
        contract_amountList.append(int(dic['contract_amount'].replace("," , "")))   # 높고 낮은 금액 비교를 위해 가래금액 안 쉼표 없애고 인트타입으로 바꿔서 리스트에 담기
    # print(contract_amountList)
    maxValue = max(contract_amountList)
    minValue = min(contract_amountList)
    # print(maxValue)
    # print(minValue)
    max_min_list = []
    for dic in list:
        if int(dic['contract_amount'].replace("," , "")) == maxValue:
            max_min_list.append(dic)
        if int(dic['contract_amount'].replace("," , "")) == minValue:
            max_min_list.append(dic)
    return max_min_list
# print(max_min_list())
from collections import Counter
# [3] OO 구별 거래량 수 계산해서 출력
def totaltradingvolume():
    newList = []    # 시군구만 뽑고 공백 기준으로 잘라서 구만 넣을 리스트
    for dic in list:
        newList.append(dic['location'].split(" ")[1])
    # print(newList)
    collec = dict(Counter(newList))
    # print(type(collec))
    return collec
    # print(collec)

# print(totaltradingvolume())

# [4] 단지명 별로 거래량을 계산 하여 거래량이 많은 단지명 TOP10 계산 하여 출력
def top_ten_transaction():
    newList = []  # 시군구만 뽑고 공백 기준으로 잘라서 구만 넣을 리스트
    for dic in list:
        newList.append(dic['name'])
    # print(newList)
    collec = dict(Counter(newList))
    # print(collec)
    # sorted 함수로 dictionary의 items() 메서드로 반환된 튜플을 내림차순 정렬
    collec = sorted(collec.items(), key = lambda x : x[1], reverse = True)
    print(collec)
    top_ten_list = []
    for data in collec[ : 10]:
        top_ten_list.append(data)
    print(top_ten_list)
    return top_ten_list

print(top_ten_transaction())

# [5] 년월 별 거래량 과 전월대비 증감율 계산 하여 출력 하기