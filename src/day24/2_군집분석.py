import pandas as pd
import math

# [1] 데이터 수집
retail_df = pd.read_excel('Online_Retail.xlsx')
print(retail_df.head())
print(retail_df.info())

# [2] 데이터 준비 및 탐색
# 오류 데이터 정제
retail_df = retail_df[retail_df['Quantity']>0]
retail_df = retail_df[retail_df['UnitPrice']>0]
retail_df = retail_df[retail_df['CustomerID'].notnull()]

# 'CustomerID' 자료형을 정수형으로 변환
retail_df['CustomerID'] = retail_df['CustomerID'].astype(int)
print(retail_df.info())
print(retail_df.isnull().sum())
print(retail_df.shape)

# 중복 레코드 제거
retail_df.drop_duplicates(inplace=True)
print(retail_df.shape)  # 확인

# 데이터 생성하기
# 제품수 , 거래건수 , 고객 수 알아보기
print(pd.DataFrame([{'Product':len(retail_df['StockCode'].value_counts()),
                     'Transaction':len(retail_df['InvoiceNo'].value_counts()),
                     'Customer':len(retail_df['CustomerID'].value_counts())}], columns=['Product' , 'Transaction' , 'Customer'] , index=['counts']))
# 고객 국적 확인
print(retail_df['Country'].value_counts())

# 고객의 주문횟수 , 주문총액 , 마지막 주문 후 며칠이 지났는지에 대한 정보 추출
# 주문 금액 컬럼 추가
retail_df['SaleAmount'] = retail_df['UnitPrice']*retail_df['Quantity']
print(retail_df.head())

aggregations = {
    'InvoiceNo':'count' ,
    'SaleAmount':'sum' ,
    'InvoiceDate':'max'
}
# CustomerID 기준으로 그룹하고 그룹화 기준 정하기
customer_df = retail_df.groupby('CustomerID').agg(aggregations)
customer_df = customer_df.reset_index()
print(customer_df.head())

# 컬럼 이름 변경
customer_df = customer_df.rename(columns={'InvoiceNo':'Freq' , 'InvoiceDate':'ElapsedDays'})
print(customer_df.head())

# 마지막 주문일로 얼마나 지났는지에 대한 값 저장
import datetime
customer_df['ElapsedDays'] = datetime.datetime(2011,12,10) - customer_df['ElapsedDays'] # 분석 기준 날짜 넣어주기 책에서는 2011-12-10
print(customer_df.head())
customer_df['ElapsedDays'] = customer_df['ElapsedDays'].apply(lambda x : x.days+1)
print(customer_df.head())

# 데이터 분포 조정하기
import matplotlib.pyplot as plt
import seaborn as sns

fig , ax = plt.subplots()
ax.boxplot([customer_df['Freq'] , customer_df['SaleAmount'] , customer_df['ElapsedDays']] , sym='bo')
plt.xticks([1 , 2 , 3] , ['Freq' , 'SaleAmount' , 'ElapsedDays'])
plt.show()

# 로그 함수 이용해서 값의 분포 조정
import numpy as np

customer_df['Freq_log'] = np.log1p(customer_df['Freq'])
customer_df['SaleAmount_log'] = np.log1p(customer_df['SaleAmount'])
customer_df['ElapsedDays_log'] = np.log1p(customer_df['ElapsedDays'])
print(customer_df.head())

fig , ax = plt.subplots()
ax.boxplot([customer_df['Freq_log'] , customer_df['SaleAmount_log'] , customer_df['ElapsedDays_log']] , sym='bo')
plt.xticks([1 , 2 , 3] , ['Freq_log' , 'SaleAmount_log' , 'ElapsedDays_log'])
plt.show()

# K-평균 군집화 모델을 이용하여 분속 모델 구축하기
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score , silhouette_samples
X_features = customer_df[['Freq_log' , 'SaleAmount_log' , 'ElapsedDays_log']].values

from sklearn.preprocessing import StandardScaler
X_features_scaled = StandardScaler().fit_transform(X_features)

# 엘보방법으로 클러스터 개수 k 선택하기
distortions = []

for i in range(1 , 11):
    kmeans_i = KMeans(n_clusters=i , random_state=0)    # 모델 생성
    kmeans_i.fit(X_features_scaled) # 스케일된 값으로 모델 학습
    distortions.append(kmeans_i.inertia_)

plt.plot(range(1 , 11) , distortions , marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortions')
plt.show()

# 스케일된 값과 엘보방법으로 얻은 클러스터 개수로 모델 학습
kmeans = KMeans(n_clusters=3 , random_state=0)  # 모델 생성
# 학습된 모델로 결과 예측
Y_labels = kmeans.fit_predict(X_features_scaled)
customer_df['ClusterLabel'] = Y_labels  # 예측 값 컬럼에 추가
print(customer_df.head())   # 확인
'''
   CustomerID  Freq  SaleAmount  ...  SaleAmount_log  ElapsedDays_log  ClusterLabel
0       12346     1    77183.60  ...       11.253955         5.789960             2
1       12347   182     4310.00  ...        8.368925         1.386294             1
2       12348    31     1797.24  ...        7.494564         4.343805             2
3       12349    73     1757.55  ...        7.472245         2.995732             2
4       12350    17      334.40  ...        5.815324         5.743003             0
'''