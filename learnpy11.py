"""포멧함수"""
print("I eat {0} apples.".format(3)) # 3을 문자열로 바꿔서 출력
print("I eat {0} apples.".format("five")) # "five"를 문자열로 바꿔서 출력
number = 3
print("I eat {0} apples.".format(number)) # number를 문자열로 바꿔서 출력
num1 = 10
num2 = 2
print("{0} and {1}".format(num1, num2))
print("I ate {number} cakes. so I was sick for {day} days.".format(day=200 ,number=50)) # 3과 2를 문자열로 바꿔서 출력
print("{0:<10}".format("hi")) # 10칸 확보하고 가장 왼쪽에 출력
print("{0:>10}".format("hi")) # 10칸 확보하고 가장 오른쪽에 출력
print("{0:^10}".format("hi")) # 10칸 확보하고 가운데에 출력
print("{0:=^10}".format("hi")) # 10칸 확보하고 가운데에 출력, 빈칸은 =로 채움
y = 3.37654368
print("{0:0.4f}".format(y)) # 소수점 4자리까지 출력
print("{0:10.4f}".format(y)) # 소수점 4자리까지 출력하고 10칸 확보
print("{{ and }}".format()) # 중괄호를 출력하고 싶을 때는 {{와 }}를 사용