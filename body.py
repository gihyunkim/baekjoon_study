# 백준 단계별로 풀기, brutal force 덩치

num_people = int(input())

people = []

for _ in range(num_people):
    w, h = input().split()
    w = int(w)
    h = int(h)
    people.append([w,h])

grade = {}

for i, body in enumerate(people):
    cnt = 1
    for j, body2 in enumerate(people):
        if i is not j:
            if body[0] < body2[0] and body[1]<body2[1]:
                cnt+=1
    grade[i] = cnt

for k in range(num_people):
    print(grade[k], end=' ')
