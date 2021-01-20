''' 9.1 클래스 '''
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# 클래스는 하나의 틀 붕어빵 기계

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)  #class로 부터 만들어지는 객체
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
# wraith1.clocking = True # 해당 객체에 클래스 외부에서 변수를 할당해줌 다른 객체에는 적용이 안된다.

'''9.2 메소드'''  #self의 함수를 이용
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 = {2}]".format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0} : 파괴되었습니다. ".format(self.name))
#
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
#
# firebat1.damaged(25)
# firebat1.damaged(25)

'''9.3 상속'''
# class Unit:  # 일반 유닛
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#
# class AttackUnit(Unit): # 공격 유닛
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 = {2}]".format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0} : 파괴되었습니다. ".format(self.name))
#
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
#
# firebat1.damaged(25)
# firebat1.damaged(25)

'''9.4 다중 상속'''
# class Unit:  # 일반 유닛
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#
# class AttackUnit(Unit): # 공격 유닛
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 = {2}]".format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0} : 파괴되었습니다. ".format(self.name))
#
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
#
# class flyableattackunit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_spped):
#         AttackUnit.__init__(self, damage, hp, damage)
#         Flyable.__init__(self, flying_spped)
#
# valkirie = flyableattackunit("발키리", 200, 6, 5)
# valkirie.fly("발키리", "5시")

'''9.5 메소드 오버라이딩'''
# class Unit:  # 일반 유닛
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
#
# class AttackUnit(Unit): # 공격 유닛
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 = {2}]".format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0} : 파괴되었습니다. ".format(self.name))
#
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
#
# class flyableattackunit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, damage, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)
#
# vulture = AttackUnit("벌쳐", 80, 10, 20)
# battlecruiser = flyableattackunit("배틀크루저", 500, 25, 3)
#
# vulture.move("11시")
# battlecruiser.move("2시")

