'''
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
'''

pt1 = input().split()
pt2 = input().split()
pt3 = input().split()
pt4 = []

if pt1[0] == pt2[0]:
    pt4.append(pt3[0])
    if pt3[1] == pt1[1]:
        pt4.append(pt2[1])
    else:
        pt4.append(pt1[1])
else:
    if pt1[0] == pt3[0]:
        pt4.append(pt2[0])
        if pt2[1] == pt1[1]:
            pt4.append(pt3[1])
        else:
            pt4.append(pt1[1])
    else:
        pt4.append(pt1[0])
        if pt1[1] == pt2[1]:
            pt4.append(pt3[1])
        else:
            pt4.append(pt2[1])

for i in pt4:
    print(i,end=' ')

