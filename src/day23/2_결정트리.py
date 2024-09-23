# 어종 데이터셋 : https://raw.githubusercontent.com/rickiepark/hg-mldl/master/fish.csv
# 어종명 예측하기
# 주제 : 여러 어종의 특성(Weight , Length , Diagonal , Height , Width)들을 바탕으로 어종명(Species) 예측하기
# Species : 어종명 , Weight : 무게 , Length : 길이 , Diagonal : 대각선길이 , Height : 높이 , Width : 너비
# [1] 데이터 셋
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/rickiepark/hg-mldl/master/fish.csv")
# print(data) # 확인
df = pd.DataFrame(data)
# print(df)
# [2] 7:3 비율로 훈련용과 테스트용으로 분리하기
# 독립변수/피처 , 종속변수/타겟/클래스 나누기
x = df[['Weight' , 'Length' , 'Diagonal' , 'Height' , 'Width']]
# print(x)
y = df['Species']
# print(y)
label_name = y.unique()
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x , y , test_size=0.3 , random_state=0)
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)
# [3] 결정트리 모델로 훈련용 데이터 피팅하기
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=156)
model.fit(x_train , y_train)
# [4] 훈련된 모델 기반으로 테스트용 데이터 예측하고 정확도 확인하기
# 출력예시) 개선 전 결정트리모델 정확도 : 0.625
y_predict = model.predict(x_test)
# print(y_predict)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test , y_predict)
print(f'개선 전 결정트리모델 정확도 : {accuracy}')

# [5] 최적의 하이퍼 파라미터 찾기   # params = {'max_depth' : [2 , 6 , 10 , 14] , 'min_samples_split' : [2 , 4 , 6 , 8]}
# 출력예시) 평균 정확도 : x.xxxx , 최적 하이퍼파라미터 : {'max_depth' : xx , 'min_samples_split' : xx}
from sklearn.model_selection import GridSearchCV
params = {'max_depth' : [2 , 6 , 10 , 14] , 'min_samples_split' : [2 , 4 , 6 , 8]}
grid_cv = GridSearchCV(model , param_grid=params , scoring='accuracy' , cv=5 , return_train_score=True)
grid_cv.fit(x_train , y_train)
print(f'평균 정확도 : {grid_cv.best_score_} , 최적 하이퍼 매개변수 : {grid_cv.best_params_}')
# [6] 최적의 하이퍼 파라미터 기반으로 모델 개선 후 테스트용 데이터 예측하고 예측 정확도 확인하기 # 시각화하기
# 출력예시) 개선 후 결정트리모델 정확도 : 0.xxx
model2 = DecisionTreeClassifier(max_depth=10 , min_samples_split=2)
model2.fit(x_train , y_train)
y_predict2 = model2.predict(x_test)
accuracy2 = accuracy_score(y_test , y_predict2)
print(f'개선 후 결정트리모델 정확도 : {accuracy2}')

# 차트 시각화
import matplotlib.pyplot as plt
from sklearn import tree
tree.plot_tree(model2 , feature_names=['Weight' , 'Length' , 'Diagonal' , 'Height' , 'Width'] , class_names=label_name)
plt.show()
# 콘솔 출력값 , 시각화 같이 보이도록 캡쳐 후 카톡방에 제출