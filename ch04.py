# 1. 리스트[] : 순서를 가지는 객체의 집합
#지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#(1-1) index()
#- 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

#(1-2) append()
#- 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

#(1-3) insert(idx, obj)
#- 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

#(1-4) pop()
#- 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

#(1-5) append()
#- 같은 이름의 사람이 몇 명 있는 지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#(1-6) sort() : 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#(1-7) reverse() : 역순
num_list.reverse()
print(num_list)

#(1-8) clear() : 모두 지우기
num_list.clear()
print(num_list)

#(1-9) 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

#(1-10) extend() : 리스트 확장
num_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(num_list)

# 2. 사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
#print(cabinet[5])                   #해당 key가 없으면 오류발생 후 종료
print("hi")
print(cabinet.get(5))               #해당 key가 없으면 'none' 출력
print(cabinet.get(5,"사용 가능"))     #해당 key가 없으면 '사용 가능' 출력
print("hi")

print(3 in cabinet)                 #True
print(5 in cabinet)                 #False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet.get("A-3"))
print(cabinet.get("B-100"))

#(2-2) 추가
cabinet["A-3"] = "김종국"            #update
cabinet["C-20"] = "조세호"           #insert
print(cabinet)

#(2-3) del : 삭제
del cabinet["A-3"]
print(cabinet)

#(2-4) key들만 출력
print(cabinet.keys())

#(2-5) value들만 출력
print(cabinet.values())

#(2-6) key, value 쌍으로 출력
print(cabinet.items())

#(2-7) 모두 지우기
cabinet.clear()
print(cabinet)

# 3. 튜플 : 고정된 값(값 추가, 변경 불가능)
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
print(menu)
#munu.add("생선까스") 오류발생 add()X

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 4. 집합(set) : 중복 안되고, 순서 없음.
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#(4-1) 교집합(java와 python 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#(4-2) 합집합(java 할 수 있거나 python 할 수 있는 개발자)
print(java |python)
print(java.union(python))

#(4-3) 차집합(java할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

#(4-4) 추가
#- python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#(4-4) 삭제
#- java를 잊었어요
java.remove("김태호")
print(java)

# 5. 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))         #set: {}
menu = list(menu)               #list:[]
print(menu, type(menu))
menu = tuple(menu)              #tuple:()
print(menu, type(menu))

# Quiz. 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
'''
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨프로그램을 작성하시오.

조건1: 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3: random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

#(활용 예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))   #무작위로 1개를 뽑는 것 
'''
from random import *
users = range(1, 21)    #1~20까지 숫자 생성
print(type(users))
users = list(users)

shuffle(users)
winners = sample(users, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")