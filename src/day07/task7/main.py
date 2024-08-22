# 다른 파일의 클래스 가져오기
from People import People   # People 클래스 가져오기

names = [ ]
def nameCreate( ) :
    global names
    newName = input('newName : ')
    newAge = input('newAge : ')
    person = People(newName , newAge)
    names.append(person)
    return
def nameRead( ) :
    global names
    for person in names:
        print(f'name : {person.name} , age : {person.age}')
    return
def nameUpdate(  ) :
    global names
    oldName = input('oldName : ')
    for person in names:
        if person.name == oldName:
            newName = input('newName : ')
            newAge = input('age : ')
            person.name = newName  # 해당 객체 속성 값 수정 하기.
            person.age = newAge
    return
def nameDelete( ) :
    global names
    deleteName = input('deleteName : ')
    for person in names:
        if person.name == deleteName:  # 만약에 삭제할 이름과 같으면
            names.remove(person)  # 리스트변수명.remove(객체)
            return  # 1개만 삭제하기 위해서는 삭제후 return
    return

if __name__ == "__main__":
    while True :
        ch = int( input('1.create 2.read 3.update 4.delete 5.exit : ') )
        if ch == 1 : nameCreate( )
        elif ch == 2 : nameRead( )
        elif ch == 3 : nameUpdate( )
        elif ch == 4 : nameDelete( )
        elif ch == 5 : break

