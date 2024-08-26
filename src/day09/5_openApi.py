# 연습문제 : 서울 열린데이터 광장에서 민주주의 서울 자유제안을 크롤링하여 JSON파일로 저장하시오.
import json
import urllib.parse
import urllib.request

key = "635847625479616e38345571594168"
def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            return res.read().decode('utf-8')
    except Exception as e:
        return None
def getFreeSuggestionsItem( title , start_index , end_index ):
    # 1. 출입국관광통계의 기본 URL
    base = "http://openAPI.seoul.go.kr:8088"
    # 2. 매개변수 : 인증키 , 시작 인덱스 , 마지막 인덱스
    base2 = f'/json/ChunmanFreeSuggestions'
    parameters = f'/{key}'
    parameters2 = f'/{start_index}/{end_index}/?title={urllib.parse.quote(title)}'

    url = base + parameters + base2 + parameters2# 3. 합치기
    print(f'>>>url : {url}')
    responseDecode = getRequestUrl(url) # 4. url 요청 후 응답객체 받기
    if responseDecode == None:          # 5. 만약에 응답객체가 None이면 None 반환
        return None
    else:                               # 6. 만약에 응답객체가 존재하면 json형식을 파이썬 객체로 반환 함수
        return json.loads(responseDecode)
        # PY : json.loads() JSON형식 ---> PY형식 변환 함수 # json.dumps() PY형식 ---> JSON형식(문자열타입) 변환 함수
        # JS : JSON.parse() JSON형식 ---> JS형식 변환 함수 # JSON.stringfy() JS형식 ---> JSON형식(문자열타입) 변환 함수
def getSuggestionsService(title , start_index , end_index):
    jsonResult = []  # 수집한 데이터를 저장할 리스트 객체
    jsonData = getFreeSuggestionsItem(title , start_index , end_index)

    if jsonData != None:
        # print(f'>>>jsonData : {jsonData}')  # 확인
        print(f">>>jsonData['ChunmanFreeSuggestions']['row'] : {jsonData['ChunmanFreeSuggestions']['row']}")
        for j in jsonData['ChunmanFreeSuggestions']['row'][start_index : end_index+1]:
            # print(j)
            SN = j['SN']  # 제안번호
            TITLE = j['TITLE']   # 제안제목
            CONTENT = j['CONTENT']  # 제안번호
            VOTE_SCORE = j['VOTE_SCORE']   # 제안번호
            REG_DATE = j['REG_DATE']   # 제안번호

            dic = {'SN' : SN , 'TITLE' : TITLE , 'CONTENT' : CONTENT , 'VOTE_SCORE' : VOTE_SCORE , 'REG_DATE' : REG_DATE}
            jsonResult.append(dic)
            print(jsonResult)
    return jsonResult

def main():
    jsonResult = [] # 수집한 데이터 저장할 리스트
    # 매개변수
    title = input("검색어를 입력하세요 : ")
    jsonResult = getSuggestionsService(title , 1 , 1000)
    with open(f'ChunmanFreeSuggestions-{title}.json', 'w', encoding="utf-8") as file:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        file.write(jsonFile)


if __name__ == "__main__":
    main()