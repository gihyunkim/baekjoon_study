# 백준
# 체스판 다시 칠하기


'''
M * N 크기의 보드

어떤 정사각형은 검은색, 나머지는 흰색.

이 보드를 잘라서 8*8 크기의 체스판으로 만들려한다.

검은색과 흰색이 번갈아서 칠해져 있어야 한다.

각 칸이 검은색과 흰색 중 하나로 색칠되어 있고,
변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.

'''

N, M = input().split() # M * N 크기 보드

N = int(N) # 행
M = int(M) # 열

# board 다차원 배열
board = [[0]*M for i in range(N)]

# 행마다 문자열로 넣어줌
for k in range(N):
        board[k]= input()


min = 1000000 # 최소한의 횟수


for count in range(2):
    if count == 0:
        base1 = "BWBWBWBW"
        base2 = "WBWBWBWB"
    else:
        base1 = "WBWBWBWB"
        base2 = "BWBWBWBW"
    # 어디서든 8x8을 떼어올 수 있음
    for start_row in range(N-7): # 맨 뒤에서 8개까지만 가능

        for start_col in range(M-7):
            cnt = 0  # 오류 개수

            # 제일 첫 글자.
    #        init_str = board[start_row][start_col]

            # 첫 글자가 B라면 첫 줄은 base1, 아니라면 base2가 된다.
    #        if init_str == 'BW':
    #            base1 = "BWBWBWBW"
    #            base2 = "WBWBWBWB"
    #        else: # 아니라면 그 반대.
    #            base1 = "WBWBWBWB"
    #            base2 = "BWBWBWBW"

            # 비교.

            for row in range(start_row, start_row+8): # row 8개
                if row == 0 or row % 2 == 0 : # row가 짝수(0포함)

                    sample = board[row][start_col:start_col+8] # 해당하는 row 문자열을 뽑아냄.

                    # 문자열 간 비교
                    for index in range(8):
                        if sample[index] != base1[index]:
                            cnt +=1

                else: # row가 홀수
                    sample = board[row][start_col:start_col + 8]  # row당 col 8개

                    # 문자열 간 비교
                    for index in range(8):
                        if sample[index] != base2[index]:
                            cnt += 1



            if cnt < min:
                min = cnt


print(min)




