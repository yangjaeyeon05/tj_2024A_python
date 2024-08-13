# - key와 value 한 쌍으로 가지는 자료형
# - {key1 : value1 , key2 : value2 , key3 : value3}

# (1) 딕셔너리의 형타
dic = {'name' : 'pey' , 'phone' : '010-9999-1234' , 'birth' : '1118'}
a = {1 : 'hi'}
a = {'a' : [1,2,3]}

# (2) 딕셔너리의 쌍 추가 , 삭제
    # 1. 추가 , 수정
dic['addr'] = '인천시'     # 변수명['key'] = 초기값 , 딕셔너리 내 존재하지 않는 key 이면 쌍 추가
print(dic)                # {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118', 'addr': '인천시'}
dic['name'] = 'kim'       # 변수명['key'] = 새로운값 , 딕셔너리 내 존재하는 key 이면 value 수정
print(dic)                # {'name': 'kim', 'phone': '010-9999-1234', 'birth': '1118', 'addr': '인천시'}
    # 2. 삭제
del dic['addr']           # del 변수명['key'] , 딕셔너리 내 존재하는 key 이면 쌍 삭제
print(dic)                # {'name': 'kim', 'phone': '010-9999-1234', 'birth': '1118'}
# del dic['age']            # KeyError: 'age' , 딕셔너리 내 존재하지 않는 key 이므로 예외 발생

# (3) 딕셔너리에서 key를 이용한 value 호출
print(dic['name'])      # 변수명['key'] , 딕셔너리 내 존재하는 key 이면 value 반환
# print(dic[name])      # NameError: name 'name' is not defined
# print(dic['age'])     # KeyError: 'age' , 딕셔너리 내 존재하지 않는 key 이면 예외 발생한다.
print(dic['phone'])     # 010-9999-1234

# (4) 딕셔너리 만들 때 주의할 점
    # 1. 중복된 key의 이름을 가질 수 없다. key는 중복 불가능 , value 중복 가능
a = {1 : 'a' , 1 : 'b'}
print(a)    # {1: 'b'} , key는 중복이 불가능하므로 마지막 쌍이 적용된다.
    # 2. 리스트 타입으로는 key 사용할 수 없다 , key가 변화하는 값인지 변화하지 않는 값인지가 달려있다.
# a = { [1 , 2] : 'hi'}   # TypeError: unhashable type: 'list'

# (5) 딕셔너리 관련 함수들
# 1. .keys() : 딕셔너리 내 모든 key를 객체로 반환
print(dic.keys())           # dict_keys(['name', 'phone', 'birth']) , py3.0이상 객체 반환
# 2. list(객체) : 객체를 리스트로 반환해서 반환 함수
print(list(dic.keys()))     # ['name', 'phone', 'birth']
# 3. .values() : 딕셔너리 내 모든 value를 모아 객체로 반환 함수
print(dic.values())         # dict_values(['kim', '010-9999-1234', '1118'])
print(list(dic.values()))   # ['kim', '010-9999-1234', '1118']
# 4. .items() : 딕셔너리 내 모든 쌍을 튜플로 묶은 객체로 반환 함수
print(dic.items())          # dict_items([('name', 'kim'), ('phone', '010-9999-1234'), ('birth', '1118')])
print(list(dic.items()))    # [('name', 'kim'), ('phone', '010-9999-1234'), ('birth', '1118')]
# 5. .get('key') : 딕셔너리 내 key에 해당하는 value 반환 함수
print(dic.get('name'))      # kim , 만일 딕셔너리 내 존재하는 key 이면 value 반환
print(dic.get('age'))       # None , 만일 딕셔너리 내 존재하는 key가 아니면 , dic['age'] 보다 조금 더 안정한 방법일 것 같다.
# 6. key in 딕셔너리변수명 : 딕셔너리 내 key가 존재하는지 여부 반환 함수
print('name' in dic)        # True
print('age' in dic)         # False
# 7. .clear() : 딕셔너리내 모든 쌍을 삭제한다.
dic.clear()
print(dic)      # {}











