def samsungData():
    list = []
    # 파일 열기
    f = open("삼성전자주가.csv" , 'r' ,encoding='cp949')
    data = f.read() # 파일 읽기
    print(data)
    rows = data.split('\n')  # 행 구분
    print(rows)
    for row in rows[1: len(rows) - 1]:  # 첫 줄 제외한 행 반복
        print(row)
        cols = row.split(',')
        dic = {'일자': eval(cols[0]),'종가': eval(cols[1]),'대비': eval(cols[2]),'등락률': eval(cols[3]),'시가': eval(cols[4]),
               '고가': eval(cols[5]),'저가': eval(cols[6]),'거래량': eval(cols[7]),'거래대금': eval(cols[8]),
               '시가총액': eval(cols[9]),'상장주식수': eval(cols[10])}
        print(dic)
        list.append(dic)
    return list

# print(samsungData()) # 확인