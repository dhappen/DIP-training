# ## 5-1 List []
# subway = [10,20,30]
# print(subway)
#
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
# # 조세호가 몇 번칸에 타고 있나?
# print(subway.index("조세호"))
# # 하하가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)
# # 정형돈을 유재석 조세호 사이에 태움
# subway.insert(1, "정형돈")
# print(subway)
# # 꺼내기
# print(subway.pop())
# print(subway)
# ## 5-2 Dictionary
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# cabinet[5] = "노홍철"
# print(cabinet)
# print(3 in cabinet)
# ## 5-3 tuple -> 내용물이 변하지 않음, 추가,변경xxx
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# ## 5-4 집합 (set), 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석","박명수"])
#
# print(java & python)
# print(java.intersection(python))
#
# print(java | python)
# print(java.union(python))
#
# python.add("김태호")
# print(python)
# java.remove("김태호")

##quiz
'''당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle 과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
-- 축하합니다 --

(활용 예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))
'''
from random import *
lst = list(range(1,21)) # 조건 1
shuffle(lst) #조건 2
win = sample(lst,4) # 조건3
print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(win[0]))
print("커피 당첨자: {0}".format(win[1:4]))
print("-- 축하합니다 --")

