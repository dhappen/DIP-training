''' 6-1 if '''
x = range(5)
print(x)
import numpy as np
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")
# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("더워")
# elif 10 <= temp and temp >30:
#     print("괜춘")
# else:
#     print("추워")
''' 6-2 for'''
#
# for waiting_no in range(5):
#     print("대기번호 : {0}".format(waiting_no))
# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print(customer)
''' 6-3 while'''

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 초 남았습니다".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다")
#
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}")
# customer = "토르"
# person = "unknown"
#
# while person != customer:
#     print("토르 커피가 준비되었습니다")
#     person = input("이름이 어떻게 되세요?")

''' 6-4 Continue and break'''
# absent = [2, 5] # 결석
# no_book = [7]
# for student in range(1,11): # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue   # for문에서 다음 턴으로 이동
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break      # for문을 끝낸다
#     print("{0}, 책을 읽어봐".format(student))
''' 6-5 한줄 for'''
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)
#
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
'''Quiz'''
'''당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승개과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 ( 소요시간 : 16분)

총 탑승 승객 : 2분'''
# from random import *
# count = 0
# match = " "
# for i in range(1,51):
#     time = randint(5,50)
#     if time >= 5 and time <= 15:
#         count += 1
#         match = "O"
#     print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(match, i, time))
#     match = " "
#
# print("총 탑승 승객 : {0}분".format(count))

