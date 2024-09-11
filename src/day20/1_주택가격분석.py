
# # 보스턴 주택 데이터 가져오기 #
# import pandas as pd # sklearn 1.2 이후로 제공하지 않음
# from sklearn.datasets import load_boston
# boston = load_boston
# print(boston)

import pandas as pd
import numpy as np

data_url = "http://lib.stat.cmu.edu/datasets/boston" # 보스턴 주택 정보가 있는 url
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    # 지정한 url에서 데이터를 데이터프레임으로 가져오기
    # sep="\s+" : 데이터 간의 공백으로 구분된 csv
    # skiprows=22 : 위에서부터 22행까지 생략
    # header=None : 헤더가 없다는 뜻
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

# print(data.shape) # 주택관련변수들( 독립변수 , 피처 )
# print(target.shape) # 주택가격( 종속변수 , 타킷변수 )

# 독립변수의 이름
feature_names = ['CRIM', 'ZN', 'INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
# 독립변수 데이터와 독립변수의 이름으로 데이터프레임 생성
boston_df = pd.DataFrame(data , columns=feature_names)
# print(boston_df.head())
# 4. 데이터프레임의 주택가격 열 추가
boston_df['PRICE'] = target
# print(boston_df.head())
# print(boston_df.shape) # (506, 14) # ( 행개수 , 열개수 )
# print(boston_df.info) # 열이름 , 열의 데이터수 , 데이터 타입 ,메모리

################# [2] 분석 모델 구축 #########################
# 1. 타겟과 피처 분할하기
Y = boston_df['PRICE'] # 종속변수 , 타겟
X = boston_df.drop(['PRICE'] , axis=1 , inplace=False) # 독립변수 , 피처 # 주택 가격 외 정보
# 2. 훈련용과 평가용 분할 하기
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(X , Y , test_size=0.3 , random_state= 156)
# 훈련용독립변수 , 테스트용독립변수 , 훈련용종속변수 , 테스트용종속변수 = train_test_split( 독립변수 , 종속변수 , test_size=분할비율 , random_state=난수생성시드)
# test_size=0.3 # 훈련용 70% , 테스트용 30%
print(x_train.shape) # (354, 13) 70%
print(x_test.shape) # (152, 13) 30%
# 3. 선형 회기 분석 모델 생성
from sklearn.linear_model import LinearRegression
lr = LinearRegression() # 선형 회귀 모델 객체 생성
# 4. 모델 훈련
lr.fit(x_train,y_train) # 훈련용 데이터를 이용한 모델 훈련
# print(lr.intercept_) # y절편
# print(lr.coef_)      # 회귀계수
# 5. 테스트용으로 예측하기
Y_predict = lr.predict(x_test)
# print(Y_predict) # 152 개의 가격 예측

# 6. 평가지표 확인하기( MSE , RMSE , 결정지수 , Y절편 , 회귀계수 )
# y_test # 동일한 피처 정보를 가진 실제 주택가격
# y_predict # 동일한 피처 정보를 가진 예측한 주택가격
from sklearn.metrics import mean_squared_error , r2_score
mse = mean_squared_error(y_test , Y_predict)    # mse 평가
rmse = np.sqrt(mse)                             # rmse 평가
r2 = r2_score(y_test , Y_predict)               # r2 평가
print(f'mse : {mse} , rmse : {rmse} , r2 : {r2}') # mse : 17.296915907902093 , rmse : 4.158956107955708 , r2 : 0.757226332313893
print(f'y절편 : {lr.intercept_} , 회귀 개수 : {np.round(lr.coef_ , 1)}') # np.round(값 , 자릿수) : 해당 자릿수에서 반올림 함수
# y절편 : 40.995595172164506 , 회귀 개수 : [ -0.1   0.1   0.    3.  -19.8   3.4   0.   -1.7   0.4  -0.   -0.9   0. -0.6]

###################### [3] 결과 시각화 #########################
import matplotlib.pyplot as plt
import seaborn as sns # 회귀분석 련 차트 구성

sns.regplot(x="CRIM" ,y="PRICE" , data=boston_df)
    # CRIM : 지역별 범죄 발생률 , PRICE :
    # - y절편 : 독립변수가 0일때 종속변수의 값
    # - 회귀계수 : 독립변수 1증가 할때마다 종속변수의 증감 단위 # 기울기
    # - 신뢰구간 : 좁으면 관계가 안정적이고 관계가 명확하다 해석. , 넓다면 예측이 불안정 하고 관계가 불명확 하다. 해석

fig , axs = plt.subplots(figsize= (16,16) , ncols=3 , nrows= 5) # 3칸 5줄로 구성된 다중 차트

x_feature = ['CRIM', 'ZN', 'INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
for i , feature in enumerate(x_feature) : # for 요소인덱스 , 요소값 in enumerate(리스트):
    print(i)
    print(feature)
    row = int(i/3) # 몫 i=0->0 , i=1->0 , i=2->0 , i=3->1
    col = i%3 # 나머지 i=0->0  ,  i=1->1, i=2->2 , i=3->0
    sns.regplot(x=feature , y = "PRICE" , data=boston_df ,ax=axs[row][col] )

plt.show() # 차트열기













