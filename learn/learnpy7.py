a = 'str'
print(a)
a = "str"
print(a)
a = '''str'''
print(a)
a = """str"""
print(a) #문자열을 만드는 방법
food = "Python's favorite food is perl" #문자열 안에 작은 따옴표가 있을때
print(food)
#food = 'Python's favorite food is perl' #잘못된 예
#print(food)
say = '"Python is very easy." he says.' #문자열 안에 큰 따옴표가 있을때
print(say)
#say = ""Python is very easy."" he says." #잘못된 예
#print(say)
food = 'Python\'s favorite food is perl' #역슬래시 이용
print(food)
say = "\"Python is very easy.\" he says." #역슬래시 이용
print(say)
multiline = "LIfe is too short\nYou need python" #줄바꿈 문자
print(multiline)
multiline = '''Life is too short
You need python'''
print(multiline)
multiline = """Life is too short
You need python"""
print(multiline) #따옴표 3개
"""
이스케이프 코드
\n 줄바꿈
\t 탭간격 줄떄
\\ 역슬래시 그대로 사용
\' 작은 따옴표 그대로 사용
\" 큰 따옴표 그대로 사용
\r 캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
\f 폼 피드(줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동)
\a 벨소리(스피커에서 삑소리)
\b 백 스페이스
\000 널 문자
\n, \t, \\, \', \" 말곤 잘 안씀
"""