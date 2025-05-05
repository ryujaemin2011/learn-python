import random #랜덤 라이브러리 임포트
count = 0 #정답 카운터 변수
while True: #무한반복
    a = random.randint(1, 10) #1~10 난수 a에 저장
    b = random.randint(1, 10) #1~10 난수 b에 저장
    c = input(str(a) + " + " + str(b) + " = ") #질문, 답변받기
    if not c.isdigit(): #이상한거 입력했을떄
        print("err") #에러문구 출력
        continue #4번줄로 돌아가기
    if int(c) == a + b: #정답일때
        print("O") #O 출력
        count += 1 #카운트 +1
    else: #틀렸을때
        print("x") #X 출력
        print(count) #맞힌갯수 출력
        break #종료