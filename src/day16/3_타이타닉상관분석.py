# 1. seaborn 라이브러리에 내장된 타이타닉 데이터를 가져오기
import seaborn as sns
titanic = sns.load_dataset("titanic")
print(titanic)
# 2. 내장된 데이터를 호출해서 csv 파일로 저장
titanic.to_csv("타이타닉.csv" , index=True)
# 3. 결측값(누락된 값/공백)
print(titanic.isnull().sum()) # 결측값 확인
# 4. 결측값 치환 , fillna() : null (결측) 값을 특정 값으로 채워주는 함수
    # (1) age열의 결측값을 중앙값(크기순으로 정렬된 상태에서)으로 치환
    # median() : 중앙값 반환해주는 함수
titanic['age'] = titanic['age'].fillna(titanic['age'].median())
print(titanic.isnull().sum())   # 확인 age에 결측값이 없어졌다.
    # (2) embarked 열의 결측값을 최빈값(집합의 빈도가 가장 많은 값)으로 치환
print(titanic['embarked'].value_counts())
'''
S    644
C    168
Q     77
'''
titanic['embarked'] = titanic['embarked'].fillna('S')
print(titanic.isnull().sum())   # 확인 embarked에 결측값이 없어졌다.
    # (3) embark_town 열의 결측값을 최빈값으로 치환
print(titanic['embark_town'].value_counts())
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')
print(titanic.isnull().sum())   # 확인 embark_town에 결측값이 없어졌다.
    # (4) deck 열의 결측값을 최빈값으로 치환     # 배의 갑판
print(titanic['deck'].value_counts())
titanic['deck'] = titanic['deck'].fillna('C')
print(titanic.isnull().sum())   # 확인 deck에 결측값이 없어졌다.

# 5. 데이터의 기본 정보
print(titanic.info())
# 6. survived(생존자) 속성의 레코드 개수
print(titanic.survived.value_counts())
'''
survived    생존자여부
0    549    사망자
1    342    생존자
'''
print(titanic.alive.value_counts())

# 차트
# 1. 남자 승객과 여자 승객의 생존율
import matplotlib.pyplot as plt
# 서브플롯 이용한 한번에 여러개 플롯 띄우기
f , ax = plt.subplots(1 , 2 , figsize=(10 , 5)) # 하나의 행에 2개의 열을 넣는다는 뜻 f : 행 , ax : 열
# 성별이 남자인 생존자 여부
print(titanic['survived'][titanic['sex'] == 'male'].value_counts())
# 원형차트 구성 # autopct : 원형차트내 각 조각 백분율 표시 # ax = ax[0] : 첫번째 자리 남성 ax[1] 두번째 자리 여성 # explode = [0 , 0.1] : 두번째 조각을 10% 떨어트리기
titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0 , 0.1] , autopct = '%1.1f%%' , ax = ax[0] , shadow=True)
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.pie(explode = [0 , 0.1] , autopct = '%1.1f%%' , ax = ax[1] , shadow=True)
ax[0].set_title('Survived (Male)')
ax[1].set_title('Survived (Female)')
plt.show()  # 남자승객 생존율을 18.9% 여자승객 생존율은 74.2% 확인

# 2. (객실) 등급별 생존자 수 # x축 : 등급(속성명) , hue=생존자여부(속성명) # 등급별 생존자여부의 개수 # data=데이터프레임
sns.countplot(x = 'pclass' , hue='survived' , data=titanic)
plt.title('Pclass vs Survived')
plt.show()  # 생존자는 1등급에서 가장 많고 사망자는 3등급이 가장 많다.
    # 예) 동행여부 속성(alone) 따라 생존자 수
sns.countplot(x = 'alone' , hue='survived' , data=titanic)
plt.title('Alone vs Survived')
plt.show()  # 혼자 왔을때 사망자가 더 많다.

# 상관 분석 # 연속형 데이터만 가능 # 회귀분석과 다른 점 : 예측치 없다.
    # 연속형 데이터만 가능하므로 연속형데이터 열만 추출 # .select_dtypes(include=[타입1 , 타입2])
titanic2 = titanic.select_dtypes(include=[int,float,bool])
# 연속형 데이터만 존재했을 때 상관분석 실행
titanic_corr = titanic2.corr(method='pearson')
print(titanic_corr)
# 상관계수 : 0~1 정도와 방향을 하나의 수치 요약  # 0 관계가 거의 없다. 1 관계가 강하다
    # 양의 상관관계는 한 변수가 증가하면 다른 변수도 증가한다.
    # 음의 상관관계는 한 변수가 증가하면 다른 변수는 감소한다.
# 분석 : 남자 성인은 생존과 음의 상관관계 , 객실등급은 생존과 음의 상관관계 , 혼자탑승한 경우 음의 상관관계
    # 남자가 증가하면 생존여부가 감소한다 , 객실등급이 증가하면 생존여부가 감소한다 ,
'''
survived와 pclass: 상관 계수는 -0.338으로, survived(생존 여부)와 pclass(좌석 등급) 간에는 음의 상관관계가 있습니다. 좌석 등급이 높을수록 생존 확률이 낮아질 수 있음을 의미합니다.
age와 fare: 상관 계수는 0.097로, 나이와 요금 간에는 매우 약한 양의 상관관계가 있음을 나타냅니다.
sibsp와 alone: 상관 계수는 -0.584로, 형제자매/배우자 수와 혼자 있는 여부 간에는 강한 음의 상관관계가 있습니다. 형제자매/배우자가 많을수록 혼자 있을 가능성이 낮다는 것을 의미할 수 있습니다.
adult_male와 alone: 상관 계수는 0.405로, 성인 남성과 혼자 있는 여부 간에는 중간 정도의 양의 상관관계가 있습니다. 성인 남성일수록 혼자 있을 가능성이 다소 높다는 것을 의미합니다.
'''
# 상관계수 csv 저장
titanic_corr.to_csv('타이타닉상관계수표.csv' , index=True)

# 특정한 변수 사이의 상관 계수 추출
print(titanic['survived'].corr(titanic['adult_male']))  # -0.5570800422053259
                # 종속변수                  # 독립변수
print(titanic['survived'].corr(titanic['fare']))    # 0.2573065223849622    # fare 요금
                # 종속변수                  # 독립변수






