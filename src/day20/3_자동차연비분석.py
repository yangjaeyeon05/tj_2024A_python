import numpy as np
import pandas as pd

data_df = pd.read_csv('auto-mpg.csv' , header=0 , engine='python')
print(f'데이터셋 크기 : {data_df.shape}') # 데이터셋 크기 : (398, 9)
print(data_df.head())

# 사용하지 않는 데이터 삭제
data_df = data_df.drop(['car_name' , 'origin' , 'horsepower'], axis=1 , inplace=False)
# axis=1 열방향 데이터 삭제
# inplace=False를 사용하는 경우 원본 데이터를 유지하면서 변경된 새로운 객체를 얻을 수 있어 원본 데이터를 그대로 두고 작업할 때 유용.
print(data_df.head())
print(f'데이터셋 크기 : {data_df.shape}') # 데이터셋 크기 : (398, 6)
print(data_df.info())

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error , r2_score

# X , Y 분할하기
# mpg 피처를 회귀식의 종속변수 y로 설정 , 나머지를 독립변수 x로 설정
Y = data_df['mpg']
X = data_df.drop(['mpg'] , axis=1 , inplace=False)
# print(Y)
# print(X)

# 훈련용 데이터와 평가용 데이터 분할하기
X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size=0.3 , random_state=0)
# test_size=0.3 테스트 데이터를 30% 사용한다는 뜻
# print(f'X_train : {X_train}')
# print(f'X_test : {X_test}')
# print(f'Y_train : {Y_train}')
# print(f'Y_test : {Y_test}')

# 선형 회귀 분석 : 모델 생성
lr = LinearRegression() # 객체 생성
# 선형 회귀 분석 : 모델 훈련
lr.fit(X_train , Y_train)
# print(LinearRegression())
# 선형 회귀 분석 : 평가 데이터에 대한 예측 수행 -> 예측 결과 Y_predict 구하기
Y_predict = lr.predict(X_test)
# print(Y_predict)

# 평가 지표
mse = mean_squared_error(Y_test , Y_predict)
rmse = np.sqrt(mse)
print(f'MSE : {mse} , RMSE : {rmse}')
print(f'r2_score{r2_score}')
print(f'Y 절편 값 : ' ,np.round(lr.intercept_ , 2))
print(f'회귀 계수 값' ,np.round(lr.coef_,2))

coef = pd.Series(data=np.round(lr.coef_, 2), index=X.columns)
coef.sort_values(ascending=False)   # 내림차순 정렬

import matplotlib.pyplot as plt
import seaborn as sns
fig , axs = plt.subplots(figsize=(16 , 16) , ncols=3 , nrows=2)
x_features = ['model_year' , 'acceleration' , 'displacement' , 'weight' , 'cylinders']
plot_color = ['r' , 'b' , 'y' , 'g' , 'r']
for i , feature in enumerate(x_features): #  x_features라는 리스트나 시퀀스의 각 요소와 그 요소의 인덱스를 함께 반복하는 방법 , 딕셔너리로 반환
    row = int(i/3)
    col = i%3
    sns.regplot(x = feature , y = 'mpg' , data=data_df , ax=axs[row][col] , color=plot_color[i])
plt.show()

# 연비 예측하기
print('연비를 예측하고 싶은 차의 정보를 입력하세요.')
cylinders_1 = int(input("cylinders : "))
displacement_1 = int(input("displacement : "))
weight_1 = int(input("weight : "))
acceleration_1 = int(input("acceleration : "))
model_year_1 = int(input("model_year : "))

mpg_predict = lr.predict([[cylinders_1 , displacement_1 , weight_1 , acceleration_1 , model_year_1]])
print(f'이 자동차의 예상 연비(mpg)는 {mpg_predict} 입니다.') # 이 자동차의 예상 연비(mpg)는 [41.31991868] 입니다.

