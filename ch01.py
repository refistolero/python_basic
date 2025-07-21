# 1. 숫자자료형 : 정수(양수,음수),실수,연산
print(5)
print(-10)
print(3.14)
print(5+3)
print(2*8)
print(3*(3+1))

# 2. 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# 3. boolean 자료형 : 참 / 거짓
print(5 > 10)       #False
print(5 < 10)       #True
print(True)
print(False)
print(not True)     #False
print(not False)    #True
print(not(5 > 10))  #True

# 4. 변수 : 값을 저장하는 공간
animal = "고양이"
name = "억울이"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요.")
print(name + "는 " + str(age) +"살이며, " + hobby + "을 아주 좋아해요.")    #str(정수형) : 정수형을 문자열로 변경
print(name,"는",age,"살이며,",hobby,"을 아주 좋아해요.")   #,로 출력할 때는 정수형 출력 가능하고 띄어쓰기가 포함된다.
print(name + "는 어른일까요? " + str(is_adult))

# 5. 주석
''' 여러 문장을 주석 처리 할려면 작은 따옴표(') 앞뒤로 3번 쓰면 됩니다. 
단축키는 ctrl + /  
'''

# Quiz. 변수를 이용하여 다음 문장을 출력하시요.
'''
변수명 : station
변수값 : "사당", "신도림", "인천공항" 순서대로 입력
출력 문장 : xx행 열차가 들어오고 있습니다.
'''
station1 = "사당"
station2 = "신도림"
station3 = "인천공항"
print(station1+"행 열차가 들어오고 있습니다.")
print(station2+"행 열차가 들어오고 있습니다.")
print(station3+"행 열차가 들어오고 있습니다.")