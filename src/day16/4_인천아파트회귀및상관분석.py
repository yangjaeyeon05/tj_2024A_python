# [1] 가설 : 아파트 층과 건축년도 증가하면 아파트 가격도 비싸다.
# [2] 주제 : 아파트 층과 건축년도에 따른 거래금액 추이 비교
# [3] 분석방법 : 다중 회귀분석 , 상관분석
# 1. 데이터 수집
import pandas as pd
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

data = pd.read_csv('아파트(매매)_실거래가_20240904134550.csv' , encoding='cp949' , skiprows=15 , thousands=',')
    # thousands=',' : 천단위 쉼표 생략 # 천단위를 정수타입으로 가져온다.
# 과제 : 해당 csv 파일을 분석하여 제출 (한글깨짐 무관)
# 종속변수 : 아파트 거래금액 # 독립변수 : 층 , 건축년도
Rformula = '거래금액 ~ 층 + 건축년도'
regression_result = ols(Rformula , data=data).fit()
# 회귀분석 결과
# print(regression_result.summary())

# 다중 회귀 분석 결과를 부분회귀 플롯으로 그리드 형식으로 차트
# 차트 한글깨짐 해결
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False


fig = plt.figure(figsize=(20 , 13))
sm.graphics.plot_partregress_grid(regression_result , fig=fig) # 선형모델 결과를 각 부분별 회귀 플롯을 그리드 형식으로 구성
plt.suptitle('인천광역시 아파트 회귀분석')
plt.show()

# 상관분석
# 연속형 데이터만 추출
data2 = data.select_dtypes(include=[int,float,bool])
# 연속형 데이터만 존재했을 때 상관분석 실행
data_corr = data2.corr(method='pearson')
print(data_corr)
# 상관분석 데이터 csv 파일로 저장
data_corr.to_csv('인천아파트상관계수표.csv' , index=True)



