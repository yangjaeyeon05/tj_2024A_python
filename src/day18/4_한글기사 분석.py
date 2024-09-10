# 주제 : 다음 경제 뉴스의 최신 10페이지 기사들 제목의 단어 빈도수 분석
# https://news.daum.net/breakingnews/economic?page=1 ~10
import re

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from konlpy.tag import Okt

# 1. 데이터 준비
textData = []
for page in range(1 ,11):   # 1부터 10까지 반복처리
    url = f'https://news.daum.net/breakingnews/economic?page={page}'    # 1. 크롤링할 url준비
    response = urllib.request.urlopen(url)  # 2. 지정한 url 열고 응답받기
    # print(response)
    htmlData = response.read()
    soup = BeautifulSoup(htmlData , 'html.parser')  # 3. 응답결과를 html로 파싱
    # print(soup)
    list_news2 = soup.select_one(".list_news2") # 4. 특정 클래스 파싱
    for li in list_news2.select('li'):  # 5. 특정 클래스 파싱해서 반복문 돌리기
        title = li.select_one(".tit_thumb > a").string  # 특정 클래스 파싱
        # print(title)
        textData.append(title)
# print(textData)
# 2. 품사 태깅
    # 1. 정규표현식  # 단어가 아닌 특수문자를 공백으로 치환해서 하나의 문자열로 담기
message = ''
for msg in textData:
    message += re.sub(r'[^\w]' , ' ' , msg)

    # 2. 태깅
okt = Okt()
tag_words = okt.nouns(message)
# print(tag_words)
# 3. 분석(빈도수)
    # 1. 빈도수 체크
from collections import Counter
words_Count = Counter(tag_words)
# print(words_Count)
    # 2. 상위 N개 추출
bestWords = words_Count.most_common(30)
    # 3. 딕셔너리로 변환
words_dict = {}
for tag , count in bestWords:
    if len(tag) > 1:
        words_dict[tag] = count
# print(bestWords)
# 4. 시각화(히스토그램 , 워드클라우드)
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wc = WordCloud("c:/Windows/fonts/malgun.ttf").generate_from_frequencies(words_dict)
plt.imshow(wc)
plt.show()
