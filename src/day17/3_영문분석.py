# [1] 한국학술연구학술정보원
# [2] Artificial intelligence 검색해서 해외학술논문에서 작성언어가 '영어'인 500개 논문 엑셀 다운로드 진행
# [3] Artificial 와 intelligence 를 제외한 학술논문의 제목 텍스트 빈도 수 분석하여 시각화하기

# 제출 : 시각화된 히스토그램 , 연도별 출판수 선차트 , 워드클라우드 3개 캡처해서 제출

# 모듈 호출하기
import pandas as pd
import glob
import re
from functools import reduce
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud

# 여러개의 파일명 불러오기
all_files = glob.glob('artificial Intelligence*.xls')
# print(all_files)

# 여러개 파일명에 해당하는 엑셀파일 호출해서 pd로 변환
all_files_data = []
for file in all_files:
    data_frame = pd.read_excel(file)
    # print(data_frame)
    all_files_data.append(data_frame)
# print(all_files_data)

# 데이터 프레임 합치기
all_files_data_concat = pd.concat(all_files_data , axis=0 , ignore_index=True)
# print(all_files_data_concat)

# 데이터 프레임 csv로 변환/내보내기
all_files_data_concat.to_csv('riss_ai.csv' , encoding='utf-8' , index=False)

# 데이터프레임의 제목만 추출
all_title = all_files_data_concat['제목']
# print(all_title)

# 불용어목록
stopWords = stopwords.words('english')
# print(stopWords)
# 표제어 객체 -> 나중에 쓰임
lemma = WordNetLemmatizer()


words = []
for title in all_title:
    # 영문이 아닌 것 정규표현식 이용해서 치환
    EnWords = re.sub(r"[^a-zA-z]+" , " " , str(title))
    # print(EnWords)
    # 소문자로 변환
    EnWordsToken = word_tokenize(EnWords.lower())
    # print(EnWordsToken)
    # 불용어 제거
    EnWordsTokenStop = [w for w in EnWordsToken if w not in stopWords]
    # print(EnWordsTokenStop)
    # 표제어 추출
    EnWordsTokenStopLemma = [lemma.lemmatize(w) for w in EnWordsTokenStop]
    # print(EnWordsTokenStopLemma)
    # 리스트에 넣기
    words.append(EnWordsTokenStopLemma)
# print(words)

# 2차원 리스트 1차원으로 변환
words2 = reduce(lambda x , y : x + y , words)
# print(words2)

# 리스트내 요소 개수 세기
count = Counter(words2)
# print(count)

word_count = dict()
# 빈도가 높은것만 추출해서 딕셔너리 생성
for tag , counts in count.most_common(50):
    if (len(tag) > 1):
        word_count[tag] = counts
# print(word_count)
# 두단어 제외하기
del word_count['intelligence']
del word_count['artificial']
# print(word_count)

# 히스토그램
sorted_Keys = sorted(word_count , key=word_count.get , reverse=True)
# print(sorted_Keys)
sorted_Values = sorted(word_count.values() , reverse=True)
# print(sorted_Values)

plt.bar(range(len(word_count)) , sorted_Values , align="center")
plt.xticks(range(len(word_count)) , list(sorted_Keys) , rotation=85)
plt.show()

# 결과 시각화 출판년도별 개수
all_files_data_concat['doc_count'] = 0
# print(all_files_data_concat)
summary_year = all_files_data_concat.groupby("출판일" , as_index=False)['doc_count'].count()
# print(summary_year)

plt.figure(figsize=(12 , 5))
plt.xlabel("year")
plt.ylabel("doc_count")
plt.grid(True)
plt.plot(range(len(summary_year)) , summary_year['doc_count'])
plt.xticks(range(len(summary_year)) , [text for text in summary_year['출판일']] , rotation=85)
plt.show()

# 워드클라우드
wc = WordCloud(background_color='white' , width=800 , height=600).generate_from_frequencies(word_count)
plt.imshow(wc)
plt.axis("off")
plt.show()

wc.to_file('riss_ai_wordCloud.jpg')