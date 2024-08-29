import matplotlib.pyplot as plt
import pandas as pd

# 판다스 데이터프레임 생성

data1 = [500 , 450 , 520 , 610]
data2 = [690 , 700 , 820 , 900]
data3 = [1100 , 1030 , 1200 , 1380]
data4 = [1500 , 1650 , 1700 , 1850]
data5 = [1990 , 2020 , 2300 , 2420]
data6 = [1020 , 1600 , 2200 , 2550]
index = [2015 , 2016 , 2017 , 2018 , 2019 , 2020]
total = [data1 , data2 , data3 , data4 , data5 , data6]
columns = ['1분기' , '2분기' , '3분기' , '4분기']
df = pd.DataFrame(total , index=index , columns=columns)
print(df)
# 데이터프레임 csv로 내보내기
df.to_csv('data.csv' , encoding='utf-8' , mode='w' , index=True)

# 차트생성
for i in total:
    plt.plot(columns , i)

# 차트 제목
plt.title('2015~2020 Quarterly sales')
# x축 레이블
plt.xlabel('Quarters')
# y축 레이블
plt.ylabel('sales')
# 눈금 이름
xLabel = ['first' , 'second' , 'third' , 'fourth']
plt.xticks(columns , xLabel , fontsize = 10)
# 범례
plt.legend(index)
plt.show()


