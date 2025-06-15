"""문자열 길이 구하기(공백 문자 포함)"""
a = "Life is too short"
print(len(a))
"""문자열 인덱싱과 슬라이싱"""
#인덱싱은 '가리킨다', 슬라이싱은 '잘라낸다'는 의미
a = "text str"
#    ||||||||
#번호:01234567
"""파이썬은 숫자를 0부터 센다"""
print(a[2])
print(a[-1]) #뒤에서부터 센다(뒤에서 첫번째는 -1)
"""0 과 -0 은 같으므로 print(a[0]) 과 print(a[-0])은 같다"""
print(a[0])
print(a[-0])
"""문자열 슬라이싱"""
print(a[0:2]) #2는 포함하지 않는다 즉 0<= a <2
print(a[2:6])
print(a[5:]) #5부터 끝까지
print(a[:4]) #처음부터 4까지
print(a[:]) #처음부터 끝까지
print(a[1:-3]) #-도 사용 가능
"""활용"""
a = "20250615Sunny"
year = a[0:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

a = "Pithon"
print(a)
a = a[:1] + "y" + a[2:] #문자열은 a[1] = y 이렇게 바꿀 수는 없다
print(a)