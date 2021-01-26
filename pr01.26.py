# 포맷팅
name = "jude"
age = "33"
hobby = "reading a book"
print('My name is %s. I\'m %s years old. My hobby is %s.' % (name, age, hobby))
print('My name is {}. I\'m {} years old. My hobby is {}.'.format(name, age, hobby))
print(f'My name is {name}. I\'m {age} years old. My hobby is {hobby}.')
I = f'My name is {name}. I\'m {age} years old. My hobby is {hobby}.'
print(I)

boy = {"name":"한결", "age":21, "height":173 }
print("이름:{0[name]}, 나이:{0[age]}, 키:{0[height]}".format(boy))

# 8장 연습문제 2번
s = "universe"
for i in s:
    print(i)

# 8장 연습문제 6번
sosi = "태연,서연,효연"
singer = sosi.split(",")
for c in singer:
    print(c,"사랑해")

# 8장 연습문제 7번
morning = "아침에 커피로 시작하고 밥 먹고 커피 마시고 자기 전에도 커피를 마신다."
print(morning.replace("커피", "우유"))

# 8장 연습문제 8번
number = "901231-1914983"
if int(number[7])%2 == 1:
    print(number[:2]+"년생 남자")
else: print(number[:2]+"년생 여자")

# 8장 연습문제 9번
sum = 356
avg = 89.2785
print(f'총점:{sum}, 평균:{avg:.2f}')
