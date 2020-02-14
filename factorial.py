# 팩토리얼
'''
0보다 크거나 같은 정수 N이 주어진다.
이때, N!을 출력하는 프로그램을 작성하시오.
'''

def factorial(num):
    if num == 1:
        return 1
    fact = num * factorial(num-1)
    return fact

num = int(input())
if num == 0 or num==1:
    f = 1
else:
    f = factorial(num)
print(f)


