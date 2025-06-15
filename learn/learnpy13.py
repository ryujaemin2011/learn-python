"""문자열 관련 함수들"""
a = "a;oshfjkdbgsd;oah"
print(a.count("o")) #a가 몇개 있는지 세기
print(a.find("o")) #a에서 o가 '처음' 나오는 위치(없으면 -1 반환)
print(a.index("o")) #a에서 o가 '처음' 나오는 위치(없으면 에러 발생)
print(",".join('abcd')) #abcd를 ,로 연결해서 a,b,c,d로 출력
print(",".join(['a', 'b', 'c', 'd'])) #['a', 'b', 'c', 'd']를 ,로 연결해서 a,b,c,d로 출력
a = "hi"
print(a)
print(a.upper()) #대문자로 바꾸기
a = a.upper()
print(a)
print(a.lower()) #소문자로 바꾸기
a = " hi "
print(a.lstrip()) #왼쪽 공백 제거
print(a.rstrip()) #오른쪽 공백 제거
print(a.strip()) #양쪽 공백 제거
print(a.replace("hi", "bye")) #hi를 bye로 바꾸기
a = " 1 2 3 4 5 "
print(a.split()) #공백을 기준으로 문자열 나누기(리스트로)
a = "1;2;3;4;5"
print(a.split(";")) #;를 기준으로 문자열 나누기(리스트로)
a = "hi"
print(a.isalpha()) #문자열이 알파벳으로만 이루어져 있는지 확인
print(a.isdigit()) #문자열이 숫자로만 이루어져 있는지 확인
a = "LIfe is too short"
print(a.startswith("Life")) #문자열이 Life로 시작하는지 확인
print(a.endswith("short")) #문자열이 short로 끝나는지 확인