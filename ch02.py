# 1. 연산자
print(1+1)  #2
print(3-1)  #2
print(5*2)  #10
print(6/3)  #2

print(2**3) #2^3 = 8
print(5%3)  #2(나머지)
print(10%3) #1
print(5//3) #1(몫)
print(10//3)#3

print(10 > 3)   #True
print(4 >= 7)   #False
print(10 < 3)   #False
print(5 <= 5)   #True

print(3 == 3)   #True
print(4 == 2)   #False
print(3 + 4 == 7)   #True

print(1 != 3)   #True
print(not(1 != 3))  #False

print((3 > 0) and (3 < 5))  #True
print((3 > 0) & (3 < 5))    #True

print((3 > 0) or (3 > 5))   #True
print((3 > 0) | (3 > 5))    #True

print(5 > 4 > 3)    #True
print(5 > 4 > 7)    #False

# 2. 간단한 수식
print(2 + 3 * 4)    #14
print((2 + 3) * 4)  #20
number = 2 + 3 * 4  #14
print(number)
number = number + 2 #16
print(number)
number += 2         #18
print(number)
number *= 2         #36
print(number)
number /= 2         #18
print(number)
number //= 2        #9
print(number)
number %= 2         #1
print(number)
number **= 2        #1
print(number)
number -= 1         #0
print(number)

# 3. 숫자처리함수
print(abs(-5))      #5(절대값)
print(pow(4, 2))    #4^2 = 16
print(max(5, 12))   #12(최대값)
print(min(5, 12))   #5(최소값)
print(round(3.14))  #3(반올림)
print(round(4.99))  #5

from math import *
print(floor(4.99))  #4(내림)
print(ceil(3.14))   #4(올림)
print(sqrt(16))     #4(제곱근)_4^2

# 4. 랜덤함수
from random import *
print(random())                 #0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)            #0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))       #0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)   #1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1)   #1 ~ 45 이하의 임의의 값 생성

print(randrange(1, 45)) #1 ~ 45 미만의 임의의 값 생성
print(randint(1, 45))       #1 ~ 45 이하의 임의의 값 생성

# Quiz. 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
'''
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야 함.
조건2 : 월별 날짜는 다름을 감안하야 최소 일수인 28이내로 정함.
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x일로 선점되었습니다.
'''

from random import *
day = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 "+ str(day) +"일로 선점되었습니다.")
