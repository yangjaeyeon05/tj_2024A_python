# 1. 예시
# [1] 데이터 준비
x = [[1] , [2] , [3] , [4] , [5]] # 2차원 배열
y = [2 , 4 , 5, 4 , 5]
# [2] 모델 생성 # 선형 회귀 # LinearRegression
from sklearn.linear_model import LinearRegression
model = LinearRegression()  # 선형 회귀 모델 객체 생성
# [3] 모델 훈련
model.fit(x , y)
# [4] y절편과 회귀 계수 확인
print(model.intercept_) # y절편   # 2.2   # x가 0일때 y의 값 # 독립변수가 0일 때 종속변수의 값
print(model.coef_)  # 회귀계수 (Coefficient)    # [0.6] # 독립변수가 1단위 증가할때 종속변수의 증가 단위
# [5] 예측 값 계산 # .predict(새로운독립변수)
text_x = [[6] , [4]]
result = model.predict(text_x)
print(result)   # [5.8 4.6]

# 2.
# 통계 프로세스 day15
# [1] 가설
# [2] 주제
# [3] 분석방법
# [4] 결론 및 제언
# [5] 한계점

# 머신러닝 프로세스
# [0] 주제 : 신생아 몸무게에 따른 성인 키 예측하기.
# [1] 데이터 수집
data = {
    '신생아몸무게' : [3.5 , 4.0 , 3.8 , 4.2 , 3.9] , # 태어났을때 몸무게
    '성인키' : [160 , 165 , 162 , 170 , 168]   # 성인이 되었을때 키
}
import pandas as pd
df = pd.DataFrame(data)
# print(df)

# [2] 데이터 전처리 및 훈련/데이터분할
feature = df[['신생아몸무게']]# 신생아몸무게 = 독립변수/피처/특성변수 등
target = df['성인키']# 성인키 = 종속변수/타겟/클래스 등
    # 데이터 분할
from sklearn.model_selection import train_test_split    # 모델 평가할때 사용되는 라이브러리
x_train , x_test , y_train , y_test = train_test_split(feature , target , test_size=0.2 , random_state=0)
# train_test_split(독립변수 , 종속변수 , test_size=테스트에사용할비율 , random_state=난수시드)
# test_size=0.2 : 훈련데이터를 80% 사용하고 테스트테이터를 20% 사용 설정
# x_train : 훈련 데이터에 사용할 독립변수
print(f'x_train : {x_train}')
# x_test : 테스트 데이터에 사용할 독립변수
print(f'x_test : {x_test}')
# y_train : 훈련 데이터에 사용할 종속변수
print(f'y_train : {y_train}')
# y_test : 테스트 데이터에 사용할 종속변수
print(f'y_test : {y_test}')

# [3] 모델 구축 및 학습
from sklearn.linear_model import LinearRegression   # 독립변수를 2차원 배열을 사용한다.
# 모델 구축
model = LinearRegression()  # 선형 회귀 모델 객체 생성
# 모델 학습
# model.fit(feature , target)
model.fit(x_train , y_train)    # 훈련 데이터를 사용한 모델 피팅

# [4] 모델 평가
from sklearn.metrics import mean_absolute_error
y_pred = model.predict(x_test) # 테스트 데이터를 사용하여 예측값을 구한다.
                                # 테스트 데이터 : (실제)신생아몸무게 3.8 (실제)성인키 162
                                # 신생아 몸무게 3.9를 가지고 학습모델의 예측값 구해서 예측값이 164
print(y_pred)   # [164.40384615]
MAE = mean_absolute_error(y_test , y_pred)  # (성인키)실제값 , (성인키)예측값

from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(y_test , y_pred)

import numpy as np
RMSE = np.sqrt(MSE)

from sklearn.metrics import r2_score
r2 = r2_score(y_test , y_pred)

print(f'MAE : {MAE}')  # 2.4038461538461604
print(f'MSE : {MSE}')   # 5.778476331360978
print(f'RMSE : {RMSE}') # 2.4038461538461604
print(f'r2 : {r2}') # nan 데이터가 적어서 예측이 불가능하다

# [5] 예측
    # 만약에 신생아 몸무게 3.6으로 태어났을 때 성인이 되면 키가 얼마나 될까요? 예측
    # 만약에 신생아 몸무게 4.1으로 태어났을 때 성인이 되면 키가 얼마나 될까요? 예측
newDf = pd.DataFrame({
    '신생아몸무게' : [3.6 , 4.1]
})
result = model.predict(newDf)
print(result)   # [161.02985075 168.11940299]




