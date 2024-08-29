# 목표 : 와인 속성을 분석하여 품질 등급을 예측한다.

# [1] 데이터수집 : winequality-red.csv , winequality-white.csv
# [2] 데이터준비 :
# 2-1 : csv 파일의 열 구분자를 ;세미콜론 -> ,쉼표 변경하여 csv 파일 새로 만들기
import pandas as pd
red_pd = pd.read_csv('winequality-red.csv' , sep=';' , header=0 , engine='python')
    # sep='csv구분자' # 기본값은 ,(쉼표)
    # header=0 : 첫 번째 행을 열 이름으로 지정하겠다는 뜻
white_pd = pd.read_csv('winequality-white.csv' , sep=';' , header=0 , engine='python')
# 새로운 csv 만들기
red_pd.to_csv('winequality-red2.csv' , index=False)
    # index=False : 데이터프레임에 인덱스 열은 CSV 파일에 포함하지 않는다.
white_pd.to_csv('winequality-white2.csv' , index=False)

# 2-2 데이터병합하기 , 레드와인과 화이트와인 분석하기 위해 하나로 합치기
print(red_pd.head())    # .head() : 데이터프레임의 위에서부터 5개 가져오기
# 1. 열 추가   # .insert(삽입할 위치 , column='열이름' , value=값) 0번째(첫번째) 열에 type 열 이름으로 red 값 추가
red_pd.insert(0 , column='type' , value='red')
print(red_pd.head())
print(red_pd.shape) # .shape , (1599, 13) # 행 개수와 열 개수 반환
print(red_pd.shape[0])  # 1599 # .shape[0] : 행개수 , .shape[1] : 열개수
# 2.
print(white_pd.head())
white_pd.insert(0 , column='type' , value='white')
print(white_pd.head())
print(white_pd.shape)   # (4898, 13)
# 3. 데이터프레임 합치기 , pd.concat([데이터프레임1 , 데이터프레임2])
wine = pd.concat([red_pd , white_pd])
print(wine.shape)   # (6497, 13)
# 4. 합친 와인 데이터프레임을 csv로 변환
wine.to_csv('wine.csv' , index=False)

# [3] 데이터 탐색
    # 1. 데이터프레임의 기본 정보 출력
print(wine.info())
    # 2. 기술 통계
wine.columns = wine.columns.str.replace(' ' , '_')  # - 열이름에 공백이 있으면 _(밑줄)로 변경
print(wine.head())
    # - .describe() : 속성(열)별 개수 , 평군 , std(표준편차) , 최소값 , 백분율25% , 백분율50%  , 백분율75% 최대값
print(wine.describe())
print(wine.describe()['quality'])   # 와인의 등급 통계
print(wine.describe()['quality'].tolist())  # 와인등급의 통계 리스트
    #
print(wine.quality.unique())    # [5 6 7 4 8 3 9]
print(wine['quality'].unique())    # [5 6 7 4 8 3 9]
print(sorted(wine.quality.unique()))  # [3 4 5 6 7 8 9]  # 와인등급의 중복 값 제거하고 정렬 오름차순
    #
print(wine['quality'].value_counts())   # 특정 열(등급) 별로 개수
print(wine['quality'].value_counts().tolist())  # [2836, 2138, 1079, 216, 193, 30, 5]
print(wine['quality'].value_counts().to_json())  # {"6":2836,"5":2138,"7":1079,"4":216,"8":193,"3":30,"9":5}

# [4] 데이터 모델링
    # 1. .groupby('그룹기준')['속성명']
    # type 속성으로 그룹해서 quality 속성 기술 통계 구하기
print(wine.groupby('type')['quality'].describe())
'''
        count      mean       std  min  25%  50%  75%  max
type                                                      
red    1599.0  5.636023  0.807569  3.0  5.0  6.0  6.0  8.0
white  4898.0  5.877909  0.885639  3.0  5.0  6.0  6.0  9.0
'''
    # 2. type 속성으로 그룹해서 quality 속성의 평균
print(wine.groupby('type')['quality'].mean())
    # 3. type 속성으로 그룹해서 quality 속성의 표준편차
print(wine.groupby('type')['quality'].std())
    # 4. type 속성으로 그룹해서 quality 속성의 평균 , 표준편차
print(wine.groupby('type')['quality'].agg(['mean' , 'std']))




