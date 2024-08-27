# http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship
# 1. BeautifulSoup 이용한 쿠우쿠우 전국 매장 정보 크롤링
# 2. 전국 쿠우쿠우 매장 정보(번호,매장명,연락처,주소,영업시간)
# 3. pandas 이용한 csv 파일로 변환
# 4. 플라스크를 이용한 쿠우쿠우 전국 매장 정보 반환하는 HTTP 매핑 정의한다.
    # HTTP(GET) : :5000/qooqoo
    # (3) 생성된 csv 파일 읽어서 json 형식을 반환

import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
import json
from flask import Flask

app = Flask(__name__)

def qooqoo_store(result):
    for page in range(1 , 7):  # 1 ~ 50까지 반복
        # 할리스 매장 정보 url
        url = f"http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page={page}"
        reponse = urllib.request.urlopen(url)
        htmlData = reponse.read()
        # print(htmlData) # 확인
        soup = BeautifulSoup(htmlData , "html.parser")
        # print(soup)
        tbody = soup.select('tbody')
        # print(tbody)
        for row in tbody[0].select("tr"):
            # print(f'>>> row : {row}')
            # print('end')
            tds = row.select('td')
            # print(len(tds))
            if len(tds) < 5: continue
            # print(f'>>>tds : {tds}')
            num = tds[0].string.strip(' ').strip('\n');    # print(num)
            subject = tds[1].select_one(".td-subject").select("a")[1].string.strip(' ').strip('\n').strip('\"'); # print(subject)
            contact = tds[2].select_one("a").string.strip(' '); # print(contact)
            address = tds[3].select('a')[0].string.strip(' ').strip('\"'); # print(address)
            time = tds[4].select('a')[0].string.strip(' ').strip('\"'); # print(time)
            store = [num , subject , contact , address , time]
            result.append(store)    # 리스트 안에 리스트 요소 추가 : 2차원 리스트 [ [] [] [] ]
    return

def main():
    result = []  # 할리스 매장 정보 리스트를 여러개 저장하는 리스트 변수 , 2차원 리스트
    print(">>> 쿠우쿠우 매장 크롤링 중 >>>")
    qooqoo_store(result)
    # print(result)  # 확인
    # py 리스트 객체를 DataFrame 객체로 변환
    qooqoo_tbl = pd.DataFrame(result, columns=('num', 'subject', 'contact', 'address' , 'time'))
    # DataFrame 객체를 csv 파일로 생성
    qooqoo_tbl.to_csv('qooqoo.csv', encoding='utf-8', mode='w', index=False)
    del result[:]

@app.route("/qooqoo" , methods = ["GET"])
def index():
    main()
    # csv파일 DataFrame 객체로 불러오기
    data = pd.read_csv('qooqoo.csv', encoding='utf-8', index_col=0, engine='python')
    # print(f'>>>data : {data}')
    # DataFrame 객체 json으로 변환
    df = pd.DataFrame(data)
    df_json = df.to_json(orient='index', indent=4, force_ascii=False)   # text/html; charset=utf-8
    # print(df_json)
    dataDict = df.to_dict(orient="index")   # 	application/json
    print(dataDict)
    # 파일 저장
    # with open(f'qooqoo.json', 'w', encoding='utf-8') as file:
    #     jsonFile = json.dumps(df_json, indent=4, sort_keys=True, ensure_ascii=False)
    #     file.write(jsonFile)
    return dataDict

if __name__ == "__main__":
    app.run(debug=True)
