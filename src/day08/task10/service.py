from region import Region

def personData():
    list = []
    f = open("인천광역시_부평구_인구현황.csv", 'r', encoding='cp949')
    data = f.read()
    rows = data.split('\n')  # 줄마다(요소)
    rowCount = len(rows)  # 데이터 전체 행 개수
    for row in rows[1: rowCount - 2]:
        if row:  # 만약에 데이터가 존재하면
            cols = row.split(',')
            region = Region(cols[0], int(cols[1]), int(cols[2]), int(cols[3]), cols[4])
            list.append(region)
    print(list)
    return list # 리스트 반환

print(personData())