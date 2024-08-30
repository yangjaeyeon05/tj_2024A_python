import pandas as pd
import json

df = pd.read_csv('행정동 단위 서울 생활인구(내국인).csv' , encoding='cp949' , engine='python')
print(df)
def totaldata():
    totaldata_tojson = df.transpose().to_json(force_ascii=False)
    # print(totaldata_tojson)
    result = json.loads(totaldata_tojson)
    # print(result)
    return result

def totalDescribe():
    total_describe =  df.describe().transpose().to_json(force_ascii=False)
    # print(total_describe)
    result = json.loads(total_describe)
    return result

# 행정동코드별 기술통계
def timeDescribe():
    time_describe = df.groupby('시간대구분')['총생활인구수'].describe().to_json()
    print(time_describe)
    result = json.loads(time_describe)
    return result

# 총생활인구수가 5번째까지 많은 행정도코드
def topFive():
    result = df.sort_values(by=['총생활인구수']  )
    print(result[ [ '총생활인구수' , '행정동코드']  ].tail() )
    # list = []
    # e = df[['총생활인구수', '행정동코드']]
    # print(e)
    # for i in e.values():
    #     print(i)
    #     for j in result:
    #         if df['총생활인구수'].all == j:
    #             list.append(df['행정동코드'])
    # print(list)

topFive()

# regionDescribe()
# totalDescribe()
#
# if __name__ == "__main__":
#     totaldata()