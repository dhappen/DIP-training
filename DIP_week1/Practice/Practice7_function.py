''' 7.1 함수'''
#
# def open_accoutn():
#     print("새로운 계좌가 생성되었습니다.")
#
# open_accoutn()

''' 7.2 반환값과 전달값'''
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
#
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
#     return balance + money
#
# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다".format(balance))
# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission
#
# balance = 0
# balance = deposit(balance, 1000)
# #
# # balance = withdraw(balance,500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원 이며 잔액은 {1}원 입니다.".format(commission, balance))
''' 7.3 기본값 '''
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어{2}"\
#           .format(name, age, main_lang))
#
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")
#
# def profile(name, age=17, main_lang = "파이썬"):
#     print("이름 : {0}\t나이 : {1}\t 주 사용 언어:{2}"\
#           .format(name, age, main_lang))
#
# profile("유재석")

''' 7.4 키워드 값 '''
# def profile(name, age, main_lang):
#     print(name, age, main_lang)
#
# profile(name = "유재석", main_lang = "파이썬", age = 20)
# profile(main_lang = "자바", age = 25, name = "김태호")

''' 7.5 가변 인자 '''
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
#
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
#
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
# profile("김태호", 25, "Kotlin", "Swift")

''' 7.6 지역변수, 전역변수'''
# gun = 10
#
# def checkpoint(soldiers): #경계 근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# def checkpoint_return(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
#
# print("전체 총 : {0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_return(gun,2)
# print("남은 총 : {0}".format(gun))

''' Quiz '''
''' 표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중
(성별에 따른 공식)
 남자 : 키(m) x 키(m) x 22
 여자 : 키(m) x 키(m) x 21
 
조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다. '''

# def std_weight(height, gender):
#     if gender == "male":
#         std = height/100 * height/100 * 22
#     elif gender == "female":
#         std = height/100 * height/100 * 21
#     else:
#         print("성별을 잘 못 입력하였습니다.")
#     return std
#
# height = float(input("키를 입력하세요: "))
# gender = input("성별을 입력하세요: ")
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, round(std_weight(height,gender),2)))
