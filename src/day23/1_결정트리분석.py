# 결정트리 : 로지스틱 회귀(이진분류) vs 결정트리(다중분류)
# 모델 생성하고 예측
# [1] 데이터 수집 # 데이터셋 찾는 과정
# 스마트폰으로 수집한 사람의 움직임 데이터
# 1. https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones
# 2. [다운로드] UCI HAR Dataset 폴더

import numpy as np
import pandas as pd

# print(pd.__version__)

# 3. 피처 이름 파일 읽어오기 # TXT 파일 읽어오기
feature_name_df = pd.read_csv('UCI_HAR_Dataset/UCI_HAR_Dataset/features.txt' , sep=r'\s+' , header=None , names=['index' , 'feature_name'] , engine='python')
    # 1. sep='\s+' : 공백으로 구분된 형식 파일
    # 2. header=None : 제목이 없는 파일
    # 3. names=['열이름1' , '열이름2']
# print(feature_name_df.head())
# print(feature_name_df.shape)    # (561, 2)
# 4. index 제거하고, feature_name 독립변수 이름만 리스트로 저장 # 두번째 열 모든 행을 리스트로 반환
feature_name = feature_name_df.iloc[:, 1].values.tolist()
    # 데이터프레임.iloc[행 슬라이싱]
    # 데이터프레임.iloc[행 슬라이싱 , 열번호]
    # feature_name_df.iloc[:] : 모든 행
    # feature_name_df.iloc[:, 1] : 모든 행의 두번째 열 (첫번째 열 제외)
    # .value 값 추출 # .tolist() 리스트로 반환 함수
# print(feature_name[:5])

# 5. 훈련용 , 테스트용 파일 읽어오기
X_train = pd.read_csv('UCI_HAR_Dataset/UCI_HAR_Dataset/train/X_train.txt' , delim_whitespace=True , header=None , encoding='latin-1')
X_train.columns = feature_name  # 피처(열) 이름 대입
X_test = pd.read_csv('UCI_HAR_Dataset/UCI_HAR_Dataset/test/X_test.txt' , delim_whitespace=True , header=None , encoding='latin-1')
X_test.columns = feature_name   # 피처(열) 이름 대입
Y_train = pd.read_csv('UCI_HAR_Dataset/UCI_HAR_Dataset/train/y_train.txt' , sep=r'\s+' , header=None , names=['action'] , engine='python')
Y_test = pd.read_csv('UCI_HAR_Dataset/UCI_HAR_Dataset/test/y_test.txt' , sep=r'\s+' , header=None , names=['action'] , engine='python')
# print(X_train.shape)    # (7352, 561)
# print(X_test.shape)     # (2947, 561)
# print(Y_train.shape)    # (7352, 1)
# print(Y_test.shape)     # (2947, 1)

# print(X_train.head())
# print(Y_train['action'].value_counts())
'''
    action
    6    1407
    5    1374
    4    1286
    1    1226
    2    1073
    3     986
'''
# 6. 종속변수의 데이터 레이블 파일 가져오기
label_name_df = pd.read_csv('UCI_HAR_Dataset/UCI_HAR_Dataset/activity_labels.txt' , sep=r'\s+' , header=None , names=['index' , 'label'] , engine='python')
# 7. 인덱스 제거하고 클래스 분류 값을 리스트 추출
label_name = label_name_df.iloc[: , 1].values.tolist()
# print(label_name)   #['WALKING', 'WALKING_UPSTAIRS', 'WALKING_DOWNSTAIRS', 'SITTING', 'STANDING', 'LAYING']

# 데이터 수집 정리
'''
    1. activity_labels.txt : 클래스(종속변수) 값에 따른 분류 값
    2. features.txt : 피처(독립변수) 값에 따른 필드(열) 이름
    3. 분류된 데이터 제공 vs train_test_split
        1. 훈련용
            1. X_train.txt
            2. y_train.txt
        2. 테스트용
            1. X_test.txt
            2. y_test.txt
    - 변수
        1. X_train      : 독립변수 데이터프레임 (훈련용)
        2. y_train      : 종속변수 데이터프레임 
        3. X_test       : 독립변수 데이터프레임 (테스트용)
        4. y_test       : 종속변수 데이터프레임 
        5. label_name   : 종속변수 값에 따른 분류 값 , 1(걷기) 2(계단오르기) 3(계단내려가기) 4(앉기) 5(서있기) 6(눕기)
'''
# 8. 결정트리 모델 구축하기
from sklearn.tree import DecisionTreeClassifier # 모듈 호출
dt_HAR = DecisionTreeClassifier(random_state=156)   # 결정 트리 분류 분석 객체 생성
dt_HAR.fit(X_train , Y_train)   # 피팅(학습)
# print(DecisionTreeClassifier(random_state=156))

# 9. 모델 예측 (샘플 또는 테스트 데이터)
Y_predict = dt_HAR.predict(X_test)  # 피팅된 모델이 새로운 데이터의 독립변수를 가지고 종속변수를 예측한다.
print(Y_predict)    # [5 5 5 ... 2 1 1] # 독립변수를 넣고 예측한 종속변수들

# 10. 테스트 데이터를 이용한 모델 예측 정확도 확인
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(Y_test , Y_predict)   # 정확도 확인 # 실제값(Y_test) , 예측값(Y_predict)
print(f'결정트리 예측 정확도 : {accuracy}')  # 결정트리 예측 정확도 : 0.8547675602307431  # 1에 가까울 수록 예측을 잘하고 있다.

# 11. (모델의 성능 개선) 최적의 하이퍼 매개변수 찾기 # 최적의 정확도가 높은 트리 찾기 # 정확도가 가장 높았을 때의 매개변수를 찾아보자.
# (1) 결정트리가 사용하는 하이퍼 매개변수 종류
print(dt_HAR.get_params())
print(dt_HAR.get_depth())   # 18
# {'ccp_alpha': 0.0, 'class_weight': None, 'criterion': 'gini', 'max_depth': None, 'max_features': None, 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'monotonic_cst': None, 'random_state': 156, 'splitter': 'best'}
    # depth :  트리의 깊이   # max_depth : 최대 트리의 깊이
    # criterion : 노드 결정 방식
from sklearn.model_selection import GridSearchCV
'''
# (2) 최적의 하이퍼 매개변수를 찾을 설정값을 변수 만들기
params = {
    'max_depth' : [6 , 8 , 10 , 12 , 16 , 20 , 24]  # 다양한 트리의 최대 노드 깊이를 설정
}
# (3) 다양한 하이퍼파라미터 조합을 시도해서 최적의 하이퍼파라미터를 찾는데 사용되는 모듈 , 교차 검증 제공
from sklearn.model_selection import GridSearchCV
    # cv 객체 생성
    # 미리 설정한 'params'의 'max_depth'라는 최대 노드 깊이를 교차 검증(5회)하는 cv 객체
grid_cv = GridSearchCV(dt_HAR , param_grid=params , scoring='accuracy' , cv=5 , return_train_score=True)
    # GridSearchCV(확인할트리모델객체 , param_grid=테스트할변수 ,  scoring='정확도' , cv=교차횟수)
        # scoring='accuracy' : 모델 평가 기준을 정확도 기준으로 하겠다는 뜻을 가진 속성
        # cv=5  # 교차검증  # 데이터를 5개로 나누어서 5번 반복해서 모델 학습
        # return_train_score=True  :검증 후 점수도 같이 반환하겠다는 뜻을 가진 설정
    # cv 객체 테스트
grid_cv.fit(X_train , Y_train)
    # 결과확인 # .cv_results_
print(grid_cv.cv_results_)
    # 검증 결과를 데이터 프레임 객체로 변환
cv_results_df = pd.DataFrame(grid_cv.cv_results_)
    # 필요한 열(필드) 확인
print(cv_results_df[['param_max_depth' , 'mean_test_score' , 'mean_train_score']])
    # 최적의 정확도  : .best_score_ , 최적의 하이퍼매개변수 : .best_params_ 확인
print(f'최고 평균 정확도 : {grid_cv.best_score_} , 최적 하이퍼 매개변수 : {grid_cv.best_params_}')
    # 사용처 : 다음에 모델 만들때 최적의 하이퍼 파라미터를 적용해서 만들기
        # dt_HAR = DecisionTreeClassifier(max_depth=16)
'''
# 12. (모델의 성능 개선) 최적의 하이퍼 파라미터 찾기2
params = {
    'max_depth' : [8 , 16 , 20] ,       # 트리의 최대 깊이로 검증하겠다.
    'min_samples_split' : [8 , 16 , 24] # 노드를 분할하기 위해 사용 되는 최소 샘플 수의 값들을 검증하겠다.
}
grid_cv = GridSearchCV(dt_HAR , param_grid=params , scoring='accuracy' , cv=5 , return_train_score=True)
grid_cv.fit(X_train , Y_train)
print(grid_cv.cv_results_)
cv_results_df = pd.DataFrame(grid_cv.cv_results_)
print(cv_results_df[['param_max_depth' , 'param_min_samples_split' , 'mean_test_score' , 'mean_train_score']])
print(f'최고 평균 정확도 : {grid_cv.best_score_} , 최적 하이퍼 매개변수 : {grid_cv.best_params_}')
# 최고 평균 정확도 : 0.8548794147162603 , 최적 하이퍼 매개변수 : {'max_depth': 8, 'min_samples_split': 16}

    # 예시) 개선된 모델 생성
model = DecisionTreeClassifier(max_depth=8 , min_samples_split=16)
model.fit(X_train , Y_train)    # 개선된 모델로 다시 피팅
    # 개선된 모델로 다시 테스트
Y_predict2 = model.predict(X_test)          # 예측
print(accuracy_score(Y_test , Y_predict2))  # 예측 정확도 확인

# * 결정트리 모델 시각화
import matplotlib.pyplot as plt
from sklearn import tree    # 결정트리 시각화 모듈
import seaborn as sns
tree.plot_tree(model , feature_names=feature_name , class_names=label_name)
    # tree.plot_tree(결정트리모델객체 , feature_names=[피처이름들] , class_names=[클래스레이블들])
plt.show()






