import pandas as pd
import matplotlib.pyplot as plt

# 실습1: 삼성전자의 최근 1년 시세 정보 CSV로 다운로드 받아서 판다스(데이터프레임)으로 읽어오기
# 정보데이터시스템 :
    # 1. 데이터프레임 객체 콘솔에 촐력(CSV -> 데이터프레임)
    # 2. 삼성전자의 최근 1년 시세 중 일자(x)별 종가(y)를 막대차트로 표현하시오.

# csv -> 데이터프레임
try:
    data = pd.read_csv('data_4950_20240829.csv' , encoding='utf-8' , index_col=0 , engine='python') # utf-8 기본값으로 인코딩
except Exception as e:  # utf-8 인코딩 오류이면 cp949 인코딩하기
    data = pd.read_csv('data_4950_20240829.csv', encoding='cp949', index_col=0, engine='python')
# 주의할점 : 파일들의 인코딩방식 (utf-8 , cp949 , ISO-8859 등등)
# index_col=0 첫번째 열을 index로 사용하겠다는 뜻
print(data)
# 데이터프레임['열이름']
# 데이터 프레임을 리스트로 변환하기
list = data.values.tolist()
print(list)
# 데이터 중 '종가'만 가져와서 리스트 만들기 , y
list_y = data['종가'].tolist()
print(list_y)
# 데이터 중 '일자'만 가져와서 리스트 만들기 , x , index_col=0 설정되어있지 않을 때
# list_x = data['일자'].tolist()
# print(list_x)
list_index = data.index # index_col=0 설정되어있을 때
print(list_index)
# 차트 생성
# 샘플
# x = ['2024/08/29' , '2024/08/28' , '2024/08/27']
# y = ['123123123' , '456456456' , '321321321']
# plt.bar(x , y , width=0.5 , color='blue')
# plt.plot(x , y)
plt.plot(list_index , list_y)   # 라인 차트
# plt.bar(list_index , list_y , width=0.5 , color='blue')   # 막대 차트
# 차트 제목
plt.title('samsung')
# x축 제목
plt.xlabel('date')
# y축 제목
plt.ylabel('closing price')
plt.show()




