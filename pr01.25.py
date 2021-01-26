def calcsum(n):
    '''1에서 n까지의 합계를 구해 리턴한다.'''
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

print("1~4까지의 합:",calcsum(4))
print("1~10까지의 합:",calcsum(10))
print("1~100까지의 합:",calcsum(100))

def oddcalcsum(n):
    '''1에서 n까지 중에서 홀수의 합을 구해 리턴한다.'''
    sum = 0
    for i in range(n+1):
        if i % 2 == 1:
            sum += i

        else: continue
    return sum

print('1~10까지 홀수의 합:',oddcalcsum(10))

def evencalcsum(n):
    '''1에서 n까지 중 짝수의 합을 구해 리턴한다.'''
    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += i
        else:continue
    return sum

print('1~10까지 짝수의 합:',evencalcsum(10))
print('-'*30)
print('')
price = 1000
def sale():
    global price #global 명령은 price변수를 지역변수로 생성하지 않고 전역변수로 참조한다.(웬만하면 안쓰는 것이 좋음)
    price = 2000

print(price)
sale()
print(price)
help(calcsum)
help(oddcalcsum)
help(evencalcsum)
print('-'*30)

def avg(a, b, c):
    avg = (a+b+c)/3
    return avg
a = avg(1,3,5)
print(a)
print('-'*30)

def num(*int):
    '''가변인수로 받은 수 중에서 가장 큰 수를 구하는 함수'''
    max = int[0]
    for i in int:
        if i > max:
            max = i
    return max
print(num(654,1,3,4,13,2,5,10,90,100,83,209,35,598,62))