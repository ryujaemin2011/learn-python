"""문자열 포멧"""
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3
print("I eat %d apples." % number)
num1 = 10
num2 = 2
print("%d and %s" % (num1, num2)) #이게 정석
"""문자열 포멧 코드
%s 문자열
%c 문자 1개
%d 정수
%f 부동소수(float)
%o 8진수
%x 16진수
%% 문자 % 자체
"""
#신기한놈:%s 그냥 다 됨(문자열로 지가 알아서 바꿈)
print("I have %s apples(?)." % 3.5) #3.5를 문자열로 바꿔서 출력
#print("Error is %d%." % 98) #Error is 98%가 안나오고 그냥 에러남
print("Error is %d%%." % 98) #이게 정석
"""문자열 포멧 코드+숫자"""
print("%10s" % "hi") #10칸 확보하고 가장 오른쪽에 출력
print("%-10sjane" % "hi") #10칸 확보하고 가장 왼쪽에 출력
print("%0.4f" % 3.37654368) #소수점 4자리까지 출력
print("%.4f" % 3.37654368) #같은거
print("%10.4f" % 3.37654368) #소수점 4자리까지 출력하고 10칸 확보"""