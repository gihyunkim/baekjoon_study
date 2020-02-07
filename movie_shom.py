# 영화감독 숌

N = int(input()) # nth movie


# 연속 6이 몇개인지
def triple_six(num):
    cnt = 0 # 최대 연속된 6의 수
    dummy_cnt = 0
    first = True # 첫번째로 6이외의 숫자가 나왔는가
    while True:
        residual = num % 10
        if residual==6: # 6이라면 cnt++
            dummy_cnt+=1
        else: # 연속해서 6이 3번 안나온경우 다시 0으로 돌림.
            if first:
                cnt = dummy_cnt
                dummy_cnt=0
                first=False
            elif dummy_cnt > cnt:
                cnt = dummy_cnt
                dummy_cnt = 0


        num = num//10

        if num==0:
            if dummy_cnt > cnt:
                cnt=dummy_cnt
            break

    return cnt


base = "666" # 6이 3개 있는 경우를 base로 잡음.
number = []
num_cnt = 0



for i in range(10000): # 666을 base로 0부터 시작해서 순차적으로 숫자를 붙여나감
    num1 = int(str(i) + base)
    num_cnt = triple_six(num1) # 6의 연속된 개수
    diff = num_cnt - 3
    if diff>=1: # 6이 4번 이상 연속되었다면
        num1 = num1 - int('6'*diff) # 차수에 따라 마지막 차수만큼의 자리수를 0으로 돌리고
        for j in range(num1, num1+10**diff): # 그 자리를 0부터 10*차수합까지 number에 넣어줌.
            number.append(j)
            if len(set(number)) == 10000:
                break
    elif diff==0:
        number.append(num1)
    if len(set(number)) == 10000:
        break



for n, result in enumerate(sorted(set(number))):
    if n+1 == N:
        print(result)




