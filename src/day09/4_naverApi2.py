# 연습문제 : 2_naverApi.py 참고하여 네이버 api로 블로그에서 월드컵에 대한 검색 결과를 크롤링하여 JSON 파일로 저장하시오.
import json
import urllib.parse
import urllib.request

clientId = "vkFgWXdbZfUneulMiPBq"
clientsecret = "HlKBE2kztf"
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id" , clientId)
    req.add_header("X-Naver-Client-Secret" , clientsecret)
    try:
        res = urllib.request.urlopen(req)
        print(f'>>code2 요청URL 결과상태 : {res.getcode()}')
        if res.getcode() == 200:
            # print(res.read().decode('utf-8'))
            return res.read().decode('utf-8')
    except Exception as e:
        print(e)
        return None

# url 구성하여 url 요청하여 응답객체 받고 json으로 변환
def getNaverSearch(node , srcText , page_start , display):
    base = "https://openapi.naver.com/v1/search"
    node = f'/{node}.json'
    parameters = f'?query={urllib.parse.quote(srcText)}&display={display}&start={page_start}'
    url = base + node + parameters
    print(f'>>> url : {url}')
    responseDecode = getRequestUrl(url)
    # print(f'>>>responseDecode : {responseDecode}')
    if responseDecode == None: return None
    else: return json.loads(responseDecode)

# 응답받은 객체들의 요소들을 뽑아서 딕셔너리 생성후 리스트에 넣고 반환해주기
def getPostData(post , jsonResult , cnt):
    title = post['title']
    link = post['link']
    description = post['description']
    bloggername = post['bloggername']
    bloggerlink = post['bloggerlink']
    postdate = post['postdate']

    # 딕셔너리 생성
    dic = {'title' : title , 'link' : link , 'description' : description , 'bloggername' : bloggername , 'bloggerlink' : bloggerlink , 'postdate' : postdate}
    print(f'>>>dic : {dic}')
    jsonResult.append(dic)

def main():
    node = 'blog'   # 크롤링할 대상
    srcText = input("검색어를 입력하세요 : ")    # 검색어
    cnt = 0 # 검색 결과 개수
    jsonResult = [] # 검색 결과를 정리하여 저장할 리스트

    jsonResponse = getNaverSearch(node , srcText , 1 , 100)
    print(f'>> jsonResponse : {jsonResponse}')
    total = jsonResponse['total']  # 전체 검색 결과 개수

    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1    # 응답 개수 1증가
            getPostData(post , jsonResult , cnt)
        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node , srcText , start , 100)

    print(f'전체 검색 : {total} 건')
    print(f'가져온 데이터 : {cnt} 건')

    with open(f'{srcText}-naver-{node}.json', 'w', encoding='utf-8') as file:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        file.write(jsonFile)

if __name__ == "__main__":
    main()