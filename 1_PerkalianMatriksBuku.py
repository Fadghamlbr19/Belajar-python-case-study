mat1 = [
    [5,0],
    [2,6]
]

mat2 = [
    [1,0],
    [4,2]
]

mat3 = []

for i in range(0, len(mat1)):
    row = []
    for j in range(0, len(mat1)):
        total = 0
        for k in range(0,len(mat1)):
            total = total + (mat1[i][k] * mat2[k][j])
        row.append(total)
    mat3.append(row)

for i in range(0,len(mat3)):
    for j in range(0,len(mat3)):
        print(mat3[i][j],end=" ")