# 직각삼각형
'''

과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이
직각 삼각형인것을 알아냈다.

주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

'''

import numpy as np


# 3변 중 가장 긴 길이의 index를 반환.
def max_num(array):
    max = -1
    for i in array:
        if max < i:
            max = i

    return np.where(array==max)[0][0]

# 직각삼각형인지를 검사.
def check_triangle(triangle):
    max_idx = max_num(triangle)
    pow_triangle = np.array([i**2 for i in triangle])

    sum = np.sum(pow_triangle[list([i for i in range(len(triangle)) if i != max_idx])])
    max_leng = pow_triangle[max_idx]

    if sum == max_leng:
        return True
    else:
        return False


while True:
    isTriangle=False
    triangle = np.array(input().split(), dtype=np.uint64)
    if np.sum(triangle) == 0:
        break
    isTriangle = check_triangle(triangle)
    if isTriangle:
        print("right")
    else:
        print("wrong")

