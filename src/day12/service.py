# day12 > service.py
# [1] 인천광역시 부평구 전월세 1년치 csv 수집 # 부동산 실거래가 : https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=
# [2] CSV 파일을 판다스의 데이터프레임 으로 불러오기
# [3] 데이터 탐색(기술통계)
    # 전체 기술통계 결과를 SPRING index6.html 테이블형식으로 출력  ( HTTP 매핑 임의로 정의 )
# [4] 데이터 모델링( 그룹화 )
    # 전월세 기준으로 그룹해서 전용면적의 기술통계 결과를 SPRING index6.html 테이블형식으로 [3]번 테이블 위에 출력  ( HTTP 매핑 임의로 정의 )
# [5] 추가
    # 1. 부평구의 동 명을 중복없이 출력하시오.
    # 2. 가장 거래수가 많은 단지명 을 1~5 등까지 출력하시오.

# 카카오톡방에 ip 제출
# 모듈 가져오기
import json
import pandas as pd
from flask import Flask
# csv -> 데이터프레임으로 불러오기 함수 여러군데에서 쓰기 위해서 전역으로 선언
data = pd.read_csv('아파트(전월세)_실거래가_20240829173521.csv' , header=14 , engine='python' , encoding="cp949")
# encoding="utf-8" 기본값(생략시) 안될 경우 cp949
# skiprows=스킵~행번호 : 특정 행을 제외한 csv 읽어오기
# js에서 column 이름을 읽지못해서 이름 임의 변경 , inplace=True : 기존 변수에 대입하겠다는 뜻
data.rename(columns={'월세금(만원)':'월세금만원'} , inplace=True)
data.rename(columns={'전용면적(㎡)':'전용면적'} , inplace=True)
print(data)
# 데이터 탐색 - 전체 기술통계 결과
# print(data.head())
# print(data.describe())
# 각 csv -> 데이터프레임으로 변환
first_pd = pd.read_csv('아파트(전월세)_실거래가_2022.csv' , encoding='cp949' , skiprows=15 , engine='python')
# print(first_pd)
second_pd = pd.read_csv('아파트(전월세)_실거래가_2023.csv' , encoding='cp949' , skiprows=15 , engine='python')
# print(second_pd)
third_pd = pd.read_csv('아파트(전월세)_실거래가_20240830115711.csv' , encoding='cp949' , skiprows=15 , engine='python')
# print(third_pd)
# 각 데이터프레임 합치기
totaldata = pd.concat([first_pd , second_pd , third_pd])
totaldata.rename(columns={'월세금(만원)':'월세금만원'} , inplace=True)
totaldata.rename(columns={'전용면적(㎡)':'전용면적'} , inplace=True)
print(totaldata)
# 합친 데이터 csv로 저장
totaldata.to_csv('totaldata.csv' , index=False)

def total():
    total = data.describe()
    print(f'>> total : {total}')
    # 데이터프레임 json으로 가져오기
    total_json = total.to_json(orient='index' , force_ascii=False)
    print(total_json)
    # json으로 가져온 데이터 py타입으로 변환
    result = json.loads(total_json)
    print(f'>> result1 : {result}')
    return result
# total()
# [4] 데이터 모델링( 그룹화 )
    # 전월세 기준으로 그룹해서 전용면적의 기술통계 결과를 SPRING index6.html 테이블형식으로 [3]번 테이블 위에 출력  ( HTTP 매핑 임의로 정의 )
def area():
    area = data.groupby('전월세구분')['전용면적'].describe()
    area = area.transpose() # 데이터프레임 행열 순서 바꾸기
    # print(area)
    area_json = area.to_json(orient='index', force_ascii=False)
    result = json.loads(area_json)
    # print(result)
    return result
# area()

# [5] 추가
    # 2. 가장 거래수가 많은 단지명 을 1~5 등까지 출력하시오.
def highest_trading():
    trading = data['단지명'].value_counts().head()
    print(trading)
    trading_json = trading.to_json(orient='index', force_ascii=False)
    result = json.loads(trading_json)
    # print(result)
    return result

# highest_trading()
# [5] 추가
    # 1. 부평구의 동 명을 중복없이 출력하시오.
def no_duplication():
    region = data['시군구'].unique()
    # print(type(region))
    result = region.tolist()
    # print(result)
    return result

def total1():
    # 합친 데이터 전체 기술통계
    total3year = totaldata.describe()
    print(total)
    # 기술통계 정보 json으로 변환
    total3year_tojson = total3year.to_json(orient='index' , force_ascii=False)
    print(total3year_tojson)
    # 파이썬 문자열 타입으로 변환 : JSON 형식의 문자열을 Python의 데이터 구조로 변환하는 역할
    result = json.loads(total3year_tojson)
    print(f'>> result2 : {result}')
    return result


