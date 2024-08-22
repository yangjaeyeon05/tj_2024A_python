import mod1
# [1] import 모듈이름
    # 모듈이름.함수명()
print(mod1.add(3 , 4))

# [2] from 모듈이름 import 함수명 , 함수명
from mod1 import add
add(3 , 4)   # 함수명()

# [3] from 모듈이름 import *
from mod1 import *
sub(3 , 4)

# [4]
import mod2
print(mod2.PI) # 3.141592
a = mod2.Math()
print(a)    # <mod2.Math object at 0x0000024A1369D4C0>
print(a.solv(2))    # 12.566368

print(mod2.add(3 , 4))  # 7

from mod2 import Math , PI
print(PI)   # 3.141592
b = Math()
print(b)    # <mod2.Math object at 0x0000020B398DD7F0>

# [5] 다른 패키지의 모듈 호출
from src.day06.Task6 import People
s = People()



