#Constant space
def ZeroM(M):
    flag = 0
    for i in range(len(M)):
        if M[i][0] == 0:
            flag = 1
        for j in range(len(M)):
            if M[i][j] == 0:
                M[i][0] = 0
    print(M)
    print(flag)

    for i in range(len(M)):
        if M[i][0] == 0:
            for j in range(len(M)):
                if M[i][j] == 0 and j != 0:
                    for k in range(len(M)):
                        M[k][j] = 0
                M[i][j] = 0
    
    if flag == 1:
        for i in range(len(M)):
            M[i][0] = 0

    return M

#2 sets
def ZeroM1(M):
    row = set()
    col = set()

    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] == 0:
                row.add(i)
                col.add(j)

    for i in row:
        for j in range(len(M)):
            M[i][j]=0
    
    for j in col:
        for i in range(len(M)):
            M[i][j] = 0

    return M

M = [[1,2,3],[4,5,6],[7,8,9]]     
print(ZeroM(M))
