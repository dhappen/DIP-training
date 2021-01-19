'''8.1 표준 입출력'''

# print("Python", "Java", sep =",", end=" ")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file = sys.stdout)
# # print("Python", "Java", file = sys.stderr)
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep = ":")

# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다.")

'''8.2 다양한 출력 포맷'''
# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(10000000000))
# # 소수점 출력
# print("{0:.2f}".format(5/3))

'''8.3 파일 입출력'''
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 10")
# score_file.close()
# score_file = open("score.txt", "r", encoding = "utf8")
# print(score_file.readline()) #줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()
# score_file = open("score.txt", "r", encoding = "utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()

'''8.3 pickle'''
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

'''8.4 with'''
