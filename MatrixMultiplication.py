M1 = [[5, 4, 3],
     [2, 4, 6],
     [4, 7, 9]]

M2 =  [[3, 2, 4],
     [4, 3, 6],
     [2, 7, 5]]
M3 = [[0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(M1)):
    for j in range(len(M2)):
        for k in range(len(M2)):
            M3[i][j]+= M1[i][k]*M2[k][j]
# print(M3)
print("The multiplication result of matrix A and B is: ")
for res in M3:
   print(res)