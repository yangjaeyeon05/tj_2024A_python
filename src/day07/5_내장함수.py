# 파이썬 배포본에 함께 들어있는 함수들 = 라이브러리
# import를 하지 않아도 된다.

# 1. abs(숫자) : 절대값 함수
print(f'{abs(3)} , {abs(-3)} , {abs(-1.2)}')
# 2. all(리스트/튜플/문자열/딕셔너리/집합) : 모두 참이면 참 반환하는 함수
    # 데이터들의 참과 거짓 , day02 4_불.py
print(f'{all([1,2,3])} , {all([1,2,3,0])} , {all([])}')
# 3. any(리스트/튜플/문자열/딕셔너리/집합) : 하나라도 참이면 참 반환하는 함수
print(f'{any([1,2,3])} , {any([1,2,3,0])} , {any([])}')
# 4. chr(유니코드) : 유니코드 숫자를 문자로 반환하는 함수
print(f'{chr(97)} , {chr(44032)}')  # a , 가
# 5. dir(객체) : 해당 객체가 가지는 변수나 함수를 보여주는 함수
print(f'{dir([])} , {dir({})}')
# 6. divmod(a , b) : a를 b로 나눈 몫과 나머지를 튜플로 반환
print(divmod(7 , 3))    # 몫 : 2 , 나머지 : 1
# 7. enumerate(리스트/튜플/문자열) : 인덱스 값을 포함한 객체를 반환한다.
for i , name in enumerate(['body' , 'foo' , 'bar']):
    print(i , name)
# 8. eval(문자열로 구성된 코드) :
print(eval('1+2'))  # '1+2' -> 1+2 => 3
print(eval("'hi' + 'a'"))   # hia
print(eval('divmod(4,3)'))  # (1, 1)
# 9. filter(함수 , 데이터) : 함수 내 조건이 충족하면 데이터 반환 함수 , list 타입으로 변환 가능
def positive(x):
    return x > 0

data = [1,-3,2,0,-5,6]
result = filter(positive , data)
print(list(result))     # list() : 리스트 타입으로 반환 해주는 함수
# 람다식 함수 , 함수명 = lamda 매개변수1,매개변수2 : 실행문
    # 주로 간단한 함수를 간결하게 사용한다.
add = lambda a , b : a + b # return 명령어가 없어도 결과값이 리턴된다.
print(add(3 , 4))   # 7
# filter와 람다식 활용
result = filter(lambda x : x > 0 , data) # js : data.filter(x => x > 0)
print(list(result)) # [1, 2, 6]
# 10. map(함수 , 데이터) : 함수내 실행문 데이터를 반환 함수 , list 타입으로 변환 가능
result = map(lambda x : x * 2 , data)
print(list(result)) # [2, -6, 4, 0, -10, 12]
# 11. hex(정수) : 정수를 입력받아 16진수 문자열로 반환 해주는 함수
print(hex(234))     # 0xea
print(hex(3))       # 0x3
# 12. id(object) : 객체를 입력받아 객체의 고유 주솟값을 반환 해주는 함수
a = 3
print(id(3))    # 140733168093688
print(id(a))    # 140733168093688
b = a
print(id(b))    # 140733168093688
print(id(4))    # 140733168093720
# 13. input() : 사용자의 입력을 받는 함수
# a = input()
# print(a)
# b = input("Enter : ")
# print(b)
# 14. int() : 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 반환 해주는 함수
print(int('3'))     # 3
print(int(3.4))     # 3
print(int('11' , 2))    # 3 , 2진수로 표현된 문자열을 10진수로 변환하여 반환
print(int('1A' , 16))   # 26 , 16진수로 표현된 문자열을 10진수로 변환하여 반환
# 15. isinstance(객체 , 클래스) : 입력받은 객체가 그 클래스의 인스턴스인지 판단하여 참이면 True 거짓이면 False 반환
class Person:
    pass
a = Person()
print(isinstance(a , Person))   # True
b = 3
print(isinstance(b , Person))   # False
# 16. len() : 값의 길이를 반환해주는 함수
print(len("python"))        # 6
print(len([1 , 2 , 3]))     # 3
print(len((1 , 'a')))       # 2
# 17. list() : 반복 가능한 데이터를 입력받아 리스트로 만들어 반환해주는 함수
print(list("python"))       # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1 , 2, 3)))     # [1, 2, 3]
a = [1, 2, 3]
b = list(a)                 # list 함수에 리스트를 입력하면 똑같은 리스트 반환
print(b)                    # [1, 2, 3]
# 18. max() : 인수로 반복 가능한 데이터 입력받아 최댓값을 반환해주는 함수
print(max([1 , 2 , 3]))     # 3
print(max("python"))        # y
# 19. min() : 인수로 반복 가능한 데이터 입력받아 최솟값을 반환해주는 함수
print(min([1 , 2 , 3]))     # 1
print(min("python"))        # h
# 20. oct() : 정수를 8진수 문자열로 변환하여 반환해주는 함수
print(oct(34))      # 0o42
print(oct(12345))   # 0o30071
# 21. open('파일이름' , '읽기방법') : 파일읽기와 읽기방법을 입력받아 파일객체를 반환해주는 함수
# f = open("binary_file" , "rb")  # FileNotFoundError 파일이 없음
# 22. ord() : 문자의 유니코드 숫자 값을 반환해주는 함수
print(ord('a'))         # 97
print(ord('가'))        # 44032
# 23. pow(x , y) : x를 y제곱한 결과값을 반환해주는 함수
print(pow(2, 4))    # 16
print(pow(3 , 3))   # 27
# 24. range() : 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 반환해주는 함수
    # 24-1 인수가 하나일 경우
print(list(range(5)))   # [0, 1, 2, 3, 4]
    # 24-2 인수가 2개일 경우
print(list(range(5 , 10)))  # [5, 6, 7, 8, 9] , 5부터 10 이전까지
    # 24-3 인수가 3개일 경우
print(list(range(1 , 10 , 2)))  # [1, 3, 5, 7, 9] , 1부터 9까지 숫자 사이는 2
print(list(range(0 , -10 , -1)))    # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9] , 0부터 -9 까지 숫자 사이는 -1
# 25. round() : 숫자를 입력받아 반올림해서 반환해주는 함수
print(round(4.6))   # 5
print(round(4.2))   # 4
print(round(5.678 , 2)) # 5.68 , 소수점 2자리까지만 반올림하여 표시
# 26. sorted() : 입력데이터를 정렬한 후 그 결과를 리스트로 반환해주는 함수
print(sorted([3 , 1 , 2]))          # [1, 2, 3]
print(sorted(['a' , 'c' , 'b']))    # ['a', 'b', 'c']
print(sorted("zero"))               # ['e', 'o', 'r', 'z']
print(sorted((3 , 2 , 1)))          # [1, 2, 3]
# 27. str() : 문자열 형태로 객체를 변환하여 반환해주는 함수
print(str(3))       # 3
print(str('hi'))    # hi
# 28. sum() : 입력 데이터의 합을 반환해주는 함수
print(sum([1 , 2 , 3]))     # 6
print(sum((4 , 5 , 6)))     # 15
# 29. tuple() : 반복 가능한 데이터를 튜플로 바꾸어 반환해주는 함수
print(tuple("abc"))         # ('a', 'b', 'c')
print(tuple([1 , 2 , 3]))   # (1, 2, 3)
print(tuple((1 , 2 , 3)))   # (1, 2, 3)
# 30. type() : 입력값의 자료형을 반환해주는 함수
print(type("abc"))                  # <class 'str'>
print(type([]))                     # <class 'list'>
print(type(open("test" , "w")))     # <class '_io.TextIOWrapper'>
# 31. zip() : 동일한 개수로 이루어진 데이터들을 묶어서 반환해주는 함수
print(list(zip([1, 2, 3], [4, 5, 6])))  # [(1, 4), (2, 5), (3, 6)]
print(list(zip([1 , 2 , 3] , [4, 5, 6] , [7, 8, 9])))   # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip("abc" , "def"))) # [('a', 'd'), ('b', 'e'), ('c', 'f')]


