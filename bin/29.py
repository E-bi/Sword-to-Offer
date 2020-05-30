def print_mat(s):
    R= len(s)
    C = R
    temp =[]
    row = 0
    col = 0
    while row < R & col < C:
        if row == R-1:
            for i in range(col,C):
                temp.append(s[row][i])
        elif col == C-1:
            for i in range(s[row][col]):
                pass
def spiralOrderPrint(matrix):
    tR = tC = 0
    dR = len(matrix) - 1
    dC = len(matrix[0]) - 1
    while tR <= dR and tC <= dC:
        if tR == dR:
            for i in range(tC, dC+1):
                print(matrix[tR][i], end=' ')
        elif tC == dC:
            for i in range(tR, dR+1):
                print(matcix[i][tC], end=' ')
        else:
            for i in range(tC, dC):
                print(matrix[tR][i], end=' ')
            for i in range(tR, dR):
                print(matrix[i][dC], end=' ')
            for i in range(dC, tC, -1):
                print(matrix[dR][i], end=' ')
            for i in range(dR, tR, -1):
                print(matrix[i][tC], end=' ')
        tR += 1
        tC += 1
        dR -= 1
        dC -= 1


s = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
spiralOrderPrint(s)
#print_mat(s)
