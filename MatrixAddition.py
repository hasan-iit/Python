M1 =[[1,2,3],
     [4,5,6],
     [7,8,9]
]
M2 = [[3, 16, -6],
           [9,7,-4],
           [-1,3,13]]
M3 = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(M1)):
    for j in range(len(M2)):
        M3[i][j] = M1[i][j]+M2[i][j]
print(M3)
for k in range(len(M3)):
    print(M3[k])