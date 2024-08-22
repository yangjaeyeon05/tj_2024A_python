from user import User
# 1. save
def dataSave(names) :  # 데이터를 파일내 저장하기 # 사용처 nameCreate , nameUpdate , nameDelete 함수 안에서 처리 후 실행
    # 1. 쓰기 모드 파일 객체
    f = open('names.txt' , 'w' , encoding='UTF8')     # 파일 쓰기모드로 객체 반환
    # 2. 내용구성
        # 파이썬의 객체 -> 문자열 만들고 파일 쓰기
    outstr = "" # 파일에 작성할 문자열 변수
    for user in names:
        outstr += f'{user.name},{user.age}\n'  # 딕셔너리를 CSV형식의 문자열로 변환 # ,(쉼표) 필드 구분 # \n(줄바꿈) 객체/딕셔너리 구분
    # 3. 출력
    f.write(outstr)                 # 파일객체 이용한 데이터 쓰기 # .write(데이터)
    f.close()                       # 파일객체 닫기 # 파일객체.close()
    return
# 2. load
def dataLoad() : # 파일내 데이터를 불러오기 # 사용처 while True 위에서 실행
    # 1. 읽기 모드 파일 객체
    try:
        f = open('names.txt' , 'r' , encoding='UTF8')     # 파일 읽기모드로 객체 반환    # 같은 패키지에 names.txt 파일을 직접 만들고 실행
        names = []
        var = f.read()                  # 파일내 데이터 전체 읽어오기 # 파일객체.read()
        print(var)                      # 확인
        # 파일내 문자열 -> 객체 만들고 리스트에 담기.
        lines = var.split('\n')  # 줄마다(요소)
        print(lines)
        for row in lines[: len(lines) - 1]:  # 읽어온 파일 내용을 \n 분해해서 한줄식 반복처리 # \n으로 객체 구분 중 # 마지막줄 제외
            if row:    # 만약에 데이터가 존재하면
                cols = row.split(',')
                user = User(cols[0] , cols[1])
            names.append(user)
            print(user)
        f.close()
        print(names)
        return names
    except FileNotFoundError: # 예외 처리 # 예외가 발생했을 때 실행되는 구역
        return []   # 빈 리스트 반환
