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
import json
import pandas as pd
from flask import Flask     # [1] 플라스크 모듈 가져오기
from flask_cors import CORS
# * 1년씩 csv 파일을 수집한다. 2022.csv , 2023.csv , 204.csv

# 전체 데이터프레임 객체 생성
df = pd.DataFrame() # 빈 데이터프레임
for year in range(2022 , 2025):
    df2 = pd.read_csv(f'{year}.csv' , encoding='cp949' , skiprows=15)
    print(df2.shape)    # shape : 레코드수 , 열개수확인
    df = pd.concat([df , df2])  # 기존 데이터 프레임에 새로운 데이터 프레임 연결/연장
    # encoding='utf-8' : 기본값(생략시) 안될경우 cp949
    # skiprows= 몇번째까지스킵행번호 : 특정 행을 제외한 csv 읽어오기
print(df.shape)

# print(df)
# 1. 통계 .describe()
# print(df.describe())    # count(개수) , mean(평균) , std(편차) , min(최소값) , max(최대값) , 25% , 50% , 75%
# print(df.describe().to_json)    # JSON의 형식의 문자열 변환
print(json.loads(df.describe().to_json()))    # JSON 형식의 문자열 타입을 딕셔너리(PY타입) 변환 # 플라스크의 HTTP 응답 시 전송하기 위해서

# 2. 그룹화 통계
print(json.loads(df.groupby('전월세구분')['전용면적(㎡)'].describe().to_json()))

# 3. 중복 제거
# print(df['시군구'])    # df에서 특정 열만 추출
print(df['시군구'].unique())   # (중복값을 제거한) 특정 열만 추출

# 4. 레코드 수
# print(df['단지명'].value_counts()) # df에서 특정 임의 레코드(행) 수
# print(df['단지명'].value_counts().head()) # df에서 위에서 5개만 추출 , .head()
print(json.loads(df['단지명'].value_counts().head().to_json()))

app = Flask(__name__)       # [2] 플라스크객체 만들기
CORS(app)

# [4] 플라스크 HTTP 매핑 정의
    # 1.
@app.route("/trans1" , methods = ['get'])
def trans1():
    return json.loads(df.describe().to_json())
    # 2.
@app.route("/trans2", methods=['get'])
def trans2():
    return json.loads(df.groupby('전월세구분')['전용면적(㎡)'].describe().to_json())
    # 3.
@app.route("/trans3", methods=['get'])
def trans3():
    return df['시군구'].unique().tolist()
    # 4.
@app.route("/trans4" , methods = ['get'])
def trans4():
    return json.loads(df['단지명'].value_counts().head().to_json())


if __name__ == "__main__":
    app.run(host="0.0.0.0" , debug=True)




