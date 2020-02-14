# 피보나치 수
'''
f0 = 0
f1 = 1
fn = fn-1 + fn-2

'''


def pibonachi(n):
    if n == 1:
        return 1
    if n == 0:
        return 0

    return pibonachi(n-1)+ pibonachi(n-2)

n = int(input()) # n 번째 피보나치 수
print(pibonachi(n))