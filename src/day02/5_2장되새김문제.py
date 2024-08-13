# 1. 평균 점수 구하기
a = 80
b = 75
c = 55
print((a+b+c)/3)

# 2. 홀수 , 짝수 판별하기
if (13%2) == 0:
    print('짝수')
else :
    print('홀수')

# 3. 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = '19'+pin[0:6]
num = pin[7: ]
print(yyyymmdd)
print(num)

# 4. 주민등록번호 인덱싱
print(pin[7])

# 5. 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(':' , "#")
print(b)

# 6. 리스트 역순 정렬하기
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 7. 리스트를 문자열로 만들기
a = ['Life' , 'is' , 'too' , 'short']
result = " ".join(a)
print(result)

# 8. 튜플 더하기
a = (1,2,3)
b = (4, )
a = a + b
print(a)

# 9. 딕셔너리의 키
a = dict()
print(a)
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python'   # TypeError: unhashable type: 'list'
# 딕셔너리의 키로는 변하는 값을 사용할 수 없기 때문 리스트는 수정이 가능하므로 딕셔너리로 사용할 수 없다?
a[250] = 'python'

# 10. 딕셔너리 값 추출하기
a = {'A' : 90 , 'B' : 80 , 'C' : 70}
result = a.pop('B')
print(a)
print(result)

# 11. 리스트에서 중복 제거하기
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

# 12. 파이썬변수
a = b = [1,2,3]
a[1] = 4
print(a)
print(b)
# a , b 모두 동일한 리스트 객체를 가지고 있기 때문이다.