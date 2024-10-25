def get_matrix(n,m,value):
    matrix = []
    if value <= 0:
        m = 0
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
a = get_matrix(2,2,10)
b = get_matrix(2,5,42)
c = get_matrix(4,2,13)
print(a,"\n",b,"\n",c,sep="")


