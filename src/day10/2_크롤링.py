from bs4 import BeautifulSoup   # 모듈가져오기
import urllib.request   # 모듈가져오기
import urllib.parse   # 모듈가져오기

# [실습1] https://quotes.toscrape.com/
url = "https://quotes.toscrape.com/"    # 크롤링할 url
response = urllib.request.urlopen(url) # 지정한 url 요청 후 응답 받기
htmlData = response.read()    # 응답 받은 내용물 전체 읽어오기
# print(htmlData) # 확인
soup = BeautifulSoup(htmlData , "html.parser")  # 지정한 html 문자열로 html 파싱 객체 생성
# print(soup) # 확인

# 특정 마크업/태그 파싱
quoteDivs = soup.select(".quote")
# print(quoteDivs)
for quote in quoteDivs:
    # 명언 문구만 추출
    print(quote.select_one(".text").string)
    # 각 명언 저자 추출
    print(quote.select('span')[1].select_one('small').string)   # quote.select_one(".author").string
    # 각 명언 태그 목록 추출
    atag_list = quote.select("div > a.tag")
    for a in atag_list:
        print(a.string , end=" " )
    print("\n\n")

# [실습2] https://v.daum.net/v/20240827074833139
url = "https://v.daum.net/v/20240827074833139"    # 크롤링할 url
response = urllib.request.urlopen(url) # 지정한 url 요청 후 응답 받기
htmlData = response.read()    # 응답 받은 내용물 전체 읽어오기
# print(htmlData) # 확인
soup = BeautifulSoup(htmlData , "html.parser")  # 지정한 html 문자열로 html 파싱 객체 생성
# print(soup) # 확인

# 파싱하기
# 기사 제목
print(soup.select_one(".tit_view").string)
print("\n\n")
ps = soup.select('p')
# print(ps)
# for p in ps:
#     # 본문 내용(사진제외)
#     print(p.text)
# print(soup.select_one(".news_view").text)   # .news_view 안에 자손이 있으니까 string이 아닌 text

# [실습3] https://search.naver.com/search.naver?query=%EB%B6%80%ED%8F%89%EA%B5%AC%EB%82%A0%EC%94%A8   # 부평구 날씨
url = "https://search.naver.com/search.naver?query="+urllib.parse.quote('부평구날씨')
response = urllib.request.urlopen(url)
htmlData = response.read()
# print(htmlData) # 확인
soup = BeautifulSoup(htmlData , "html.parser")
# print(soup)   # 확인
print(soup.select_one(".temperature_text"))
# 온도 추출
# <div class="temperature_text"> <strong><span class="blind">현재 온도</span>27.2<span class="celsius">°</span></strong> </div>
print(soup.select_one(".temperature_text").text)    #  현재 온도27.2°
# 습도 추출
print(soup.select_one(".summary_list").select(".sort")[1].text) #  습도 68%


