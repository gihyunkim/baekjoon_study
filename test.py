import numpy as np

x = np.array([[1,3],[2,2]])
y = np.array([[2,3],[3,3]])

print(x.shape)
print(y)

sum = np.sum(x+y,axis=0)
print(sum)