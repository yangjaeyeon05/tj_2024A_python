# 문자열 활용 , p.50 ~ p.76
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 이름을 입력받아 여러명의 이름을 저장
#          2. 저장된 여러명의 이름을 모두 출력
#          3. 수정할 이름과 새로운 이름을 입력받아 수정
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능.
# [조건4] : 최대한 리스트 타입 사용하지 않기
# 제출 : git에 commit 후 카톡방에 해당 과제가 있는 링크 제출
names = ""  # 여러개 name들을 저장하는 문자열

def nameCreate():
    newName = input("이름을 입력 해주세요 : ")
    global names
    names += newName
    return

def nameRead( ):
    print(names)
    return

def nameUpdate( ):
    name = input("수정할 이름을 입력 해주세요 : ")
    newName = input("새로운 이름을 입력 해주세요 : ")
    global names
    names = names.replace(name , newName)
    return

def nameDelete( ):
    name = input("삭제할 이름을 입력 해주세요 : ")
    global names
    names = names.replace(name , "")
    return

while True: # 무한루프
    ch = int(input("1. create 2. read 3. update 4. delete 5. exit: "))
    if ch == 1:
        nameCreate()
        print(names)
    elif ch == 2:
        nameRead()
    elif ch == 3:
        nameUpdate()
        print(names)
    elif ch == 4:
        nameDelete()
        print(names)
    elif ch == 5:
        break



