# day07 > task9 > main.py
'''
    csv파일 다루기
    파일 : 인천광역시_부평구_인구현황.csv
    [조건1] 부평구의 동 마다 Region 객체 생성 해서 리스트 담기
    [조건2]
        Region 객체 변수 :
            1.동이름 2.총인구수 3.남인구수 4.여인구수 5.세대수
        Region 함수
            1. 남자 비율 계산 함수
            2. 여자 비율 계산 함수
    [조건3] 모든 객체의 정보를 f포메팅 해서 console 창에 출력하시오.
    [조건4] 출력시 동 마다 남 여 비율 계산해서 백분율로 출력하시오.
    [출력예시]
        부평1동       35141,  16835,  18306,  16861   59%     41%
        부평2동       14702,  7289,   7413,   7312    51%     49%
        ~~~~~~
'''
from region import Region
if __name__ == "__main__" :
    print('--start--')
    f = open("인천광역시_부평구_인구현황.csv" , 'r')
    list = []
    var = f.read()
    # print(var)
    lines = var.split('\n')  # 줄마다(요소)
    for row in lines[1 : len(lines) - 2]:  # 읽어온 파일 내용을 \n 분해해서 한줄식 반복처리 # \n으로 객체 구분 중 첫째줄 제외 , 마지막부터 2번째까지 제외
        # print(row)
        if row:  # 만약에 데이터가 존재하면
            cols = row.split(',')
            region = Region(cols[0], cols[1] , cols[2] , cols[3] , cols[4]) # 객체 변수에 맞는 값 저장하고
            region.남비 = region.남자비율(int(cols[2]) , int(cols[1]))    # 프린트할 남자비율과
            region.여비 = region.여자비율(int(cols[3]) , int(cols[1]))    # 여자비율 구해서
            list.append(region)                                         # 리스트에 저장
    for line in list:
        print(f'{line.동이름:<5} {line.총인구수:<6} {line.남인구수:<5} {line.여인구수:<5} {line.세대수:<5} {line.남비}% {line.여비}%')