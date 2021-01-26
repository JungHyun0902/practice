# 178 ~ 185
# count
s = '''생각이란 생각할 수록 생각나므로 생각하지 말아야 할 생각은 생각하지
않으려고 하는 생각이 옳은 생각이라고 생각합니다.'''
print("생각의 출현 횟수:", s.count('생각'))
#-> 생각의 출현 횟수: 9

# in
s = 'python programming'
print('a' in s)
print('z' in s)
print('pro' in s)
print('x' not in s)

'''
-> 
True
False
True
True
'''

# startswith
name = '김정현'
if name.startswith('김'):
    print('김가입니다.')
if name.startswith('박'):
    print('박가입니다.')

file = "girl.jpg"
if file.endswith('.jpg'):
    print('그림 파일입니다.')
'''
->
김가입니다.
그림 파일입니다.
'''

# isdecimal(모든 문자가 숫자인지 조사한다.)
height = input("키를 입력하세요:")
if height.isdecimal():
    print("키 =", height)
else: print("숫자만 입력하세요.")

# lower , upper
s = "Good morning. my love KIM."
print(s.lower())
print(s.upper())
print(s)

print(s.swapcase()) # 대문자는 소문자로, 소문자는 대문자로 변환
print(s.capitalize())
print(s.title()) # 문자열의 단어 첫 문자들만 대문자로 변환
'''
->
good morning. my love kim.
GOOD MORNING. MY LOVE KIM.
Good morning. my love KIM.
gOOD MORNING. MY LOVE kim.
Good morning. my love kim.
Good Morning. My Love Kim.

'''

# strlower
python = input("파이썬의 영문 철자를 입력하시오:")
if python.lower() == 'python':
    print("You're right~!")
'''
파이썬의 영문 철자를 입력하시오:PyThon
You're right~!
'''

# strip
s = "  angel  "
print(s + "님")
print(s.lstrip()+"님") # 왼쪽 공백 제거
print(s.rstrip()+"님") # 오른쪽 공백 제거
print(s.strip()+"님") # 양쪽 공백 제거
'''
  angel  님
angel  님
  angel님
angel님
'''

# split (구분자를 기준으로 문자열을 분할함. 하나의 문자열이 여러 개의 부분 문자열로 쪼개져 리스트에 저장됨.)
s = "짜장 짬뽕 탕수육"
print(s.split())

s2 = "서울->대전->대구->부산"
city = s2.split("->")
print(city)
for c in city:
    print(c, "찍고", end=' ')
'''
['짜장', '짬뽕', '탕수육']
['서울', '대전', '대구', '부산']
서울 찍고 대전 찍고 대구 찍고 부산 찍고
'''
print(' ')
#splitlines(개행문자나 파일 구분자, 그룹 구분자 등을 기준으로 문자열을 잘라 리스트로 만듬. )
traveler = '''강나루 건너서\n밀밭 길을\n\n구름에 달 가듯이\n가는 나그네\n
길은 외줄기\n남도 삼백리\n\n술 익는 마을마다\n타는 저녁놀\n
구름에 달 가듯이\n가는 나그네'''
# 그냥 출력해도 결과는 같지만 행별로 나누어 놓으면 각 행에 대한 개별적인 처리가 가능함.
# ex. 행렬로 번호를 붙인다거나 정렬을 다르게 지정.
poet = traveler.splitlines()
for line in poet:
    print(line)
'''
강나루 건너서
밀밭 길을

구름에 달 가듯이
가는 나그네

길은 외줄기
남도 삼백리

술 익는 마을마다
타는 저녁놀

구름에 달 가듯이
가는 나그네

'''

# join(문자열의 각 문자 사이에 다른 문자열을 끼워 넣음)
s = "._."
print(s.join("대한민국"))
# 대._.한._.민._.국 (join 메서드를 호출하는 문자열이 삽입 대상임을 유의!)

# splitjoin
s2 = "서울->대전->대구->부산"
city = s2.split("->")
print(" 찍고 ".join(city)) # 서울 찍고 대전 찍고 대구 찍고 부산
