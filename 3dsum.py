import numpy as np
arr = []
dim1 = int(input('Enter the first Dimension scale:'))
dim2 = int(input('Enter the second Dimension scale:'))
dim3 = int(input('Enter the third Dimension scale:'))
sum = 0
arr = np.zeros((dim1,dim2,dim3))
for k in range(dim3):
    for i in range(dim1):
        for j in range(dim2):
            arr[i][j][k]= int(input('Enter a value:'))
    for i in range(dim1):
        for j in range(dim2):
            sum += arr[i][j][k]
print(sum)