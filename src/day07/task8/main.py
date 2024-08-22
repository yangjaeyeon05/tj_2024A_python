'''
    user.py : user 객체의 클래스 정의
    file.py : save() , load() 함수를 정의
    [조건1] 이름과 나이를 입력받아 저장
    [조건2] 프로그램이 종료되고 다시 실행해도 names 데이터가 유지되도록 파일처리
'''
from user import User
from file import *

names = [ ]
def nameCreate( ) :
    global names
    newName = input('newName : ')
    newAge = input('newAge : ')
    user = User(newName , newAge)
    names.append(user)
    # 파일처리 , 저장하기
    dataSave(names)
    return
def nameRead( ) :
    global names
    for user in names:
        print(f'name : {user.name} , age : {user.age}')
    return

if __name__ == "__main__" :
    names = dataLoad() # 파일처리 , 불러오기
    while True :
        ch = int( input('1.create 2.read : ') )
        if ch == 1 : nameCreate( )
        elif ch == 2 : nameRead( )