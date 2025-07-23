# 1. 문자열
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)

# 2. 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연도 : " + jumin[0:2])     #0부터 2직전까지 (0,1)
print("월 : " + jumin[2:4])
print("월 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])   #처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:])   #7부터 끝까지
print("뒤 7자리(뒤부터) : " + jumin[-7:])     #맨 뒤에서 7번째부터 끝까지

# 3. 문자열 처리함수
python = "Python is Amazing"
print(python.lower())       #소문자
print(python.upper())       #대문자
print(python[0].isupper())  #첫번째 문자가 대문자면 True
print(len(python))          #문자길이
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)                #5
index = python.index("n", index + 1)    #첫번째 문자n 다음의 문자n의 인덱스
print(index)

print(python.find("n"))
print(python.find("Java"))   #-1 : 내가 원하는 값이 변수에 없으면 -1
#print(python.index("Java")) #오류 : 내가 원하는 값이 변수에 없으면 오류 발생하고 종료
print("hi")

print(python.count("n"))    #n이 몇 개 있는지

# 4. 문자열 포맷
print("a" + "b")
print("a", "b")
#(4-1)방법1
print("나는 %d살입니다." % 20)            #%d 정수
print("나는 %s살입니다." % "30")          #%s 문자열
print("나는 %s을 좋아해요." % "파이썬")    #%s 문자열
print("Apple은 %c로 시작해요." % 'A')     #%c 문자

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

#(4-2)방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

#(4-3)방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))

#(4-4)방법4 python v3.6이상
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 5. 탈출문자
''' 오류 발생
print("백문이 불여일견
      백견이 불여일타")
'''
print ("백문이 불여일견\n백견이 불여일타")    #\n : 줄바꿈

# 저는 "회사원"입니다.
print ('저는 "회사원"입니다.')
print ("저는 \"회사원\"입니다.")            #\" : 문장 내에서 따옴표

print("C:\\Users\\python")               #\\ : 문장 내에서 \

print("Red Apple\rpine")                 #\r : 커서를 맨 앞으로 이동****

print("Redd\bApple")                     #\b : 백스페이스(한 글자 삭제)

print("Red\tApple")                      #\t : 탭

# Quiz. 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.
'''
예) http://naver.com
규칙1: http:// 부분은 제외 => naver.com
규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
            (nav)               (5)         (1)
예) 생성된 비밀번호 : nav51!
'''
#url = "http://naver.com"
url = "http://google.com"
print(url)
site = url[7:]
#site = url.replace("http:// ", "")             #*****
print(site)
pointIdx = site.find(".")
#print(pointIdx)
name = site[:pointIdx]                          #규칙2
#print(name)
password = name[:3] + str(len(name))+str(name.count('e'))+"!"
print(password)
print("{0}의 비밀번호는 {1}입니다.".format(url, password))