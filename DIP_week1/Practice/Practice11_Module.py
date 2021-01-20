''' 11.1 모듈'''

# import Theater_module
#
# Theater_module.price(3)
# Theater_module.price_morning(2)
# Theater_module.price_soldier(4)
# import Theater_module as mv
#
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)
#
# from Theater_module import *
# price(3)
# from Theater_module import price, price_morning
#
# price(4)

'''11.2 패키지'''

# import Travel.thailand
# trip_to = Travel.thailand.ThailandPackage()
# trip_to.detail()

'''11.3 __all__'''
#
# from Travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

'''11.4 패키지 모듈 위치'''

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

'''11.5 내장 함수'''
'''input() : 사용자 입력을 받는 함수'''

'''dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시 '''
#
# import random
# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))

'''os : 운영체제에서 제공하는 기본 기능'''
import os
# print(os.getcwd()) # 현재 디렉토리
#
# folder = "sample_dir"
#
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

'''time : 시간 관련 함수'''
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td)