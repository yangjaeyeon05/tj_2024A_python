# 주제 : 커피 매장의 주소를 이용한 지도에 마커 표시하기
# 실습파일 준비 : CoffeeBean.csv
import json

# 1. 데이터 수집
import pandas as pd
df = pd.read_csv('CoffeeBean.csv' , encoding='cp949' , index_col=0) # index_col=0 : 첫 번째 열(인덱스 0)을 DataFrame의 인덱스로 사용하겠다는 뜻
print(df)

# 2. 데이터 가공 # 주소 데이터를 행정구역 주소 체계에 맞게 정리 # 실습 제외
# 3. 포리움 제외 # 지도 시각화는 카카오 지도로 실습

import json
# 플라스크
from flask import Flask
app = Flask(__name__)

from flask_cors import CORS
CORS(app)

@app.route("/")
def index():
    # df 객체를 json으로 반환
    jsonData = df.to_json(orient="records" , force_ascii=False)
    # json형식을 py형식으로 변환
    result = json.loads(jsonData)
    return result

if __name__ == '__main__':
    app.run(debug=True)

