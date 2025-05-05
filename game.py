import random #랜덤 라이브러리 임포트
import time #시간 라이브러리 임포트
count = 0 #정답 카운터 변수
while True: #무한반복
    a = random.randint(1, 10) #1~10 난수 a에 저장
    b = random.randint(1, 10) #1~10 난수 b에 저장
    start = time.time() #시간 측정 시작
    c = input(str(a) + " + " + str(b) + " = ") #질문, 답변받기
    if not c.isdigit(): #이상한거 입력했을떄
        print("숫자를 입력하세요") #에러문구 출력
        continue #4번줄로 돌아가기
    if int(c) == a + b: #정답일때
        end = time.time() #시간 측정 종료
        print("걸린시간 : " + str(round(end - start, 2))) #걸린시간 알려줌
        print("정답") #'정답' 출력
        count += 1 #카운트 +1
    else: #틀렸을때
        print("오답") #'오답' 출력
        print("정답 : " + str(a + b)) #정답 알려줌
        print("맞힌갯수 : " + str(count)) #맞힌갯수 출력
        break #종료