def GetMax(mat):
    if (not mat) or len(mat)==0 or (not mat[0]) or len(mat[0])==0:
        return
    C = len(mat)
    R = C
    #buff表示从左上角走到位置为(i,j)处最大路径的和
    buff = [[0 for i in range(len(mat))] for j in range(len(mat[0]))] 
    buff[0][0] = mat[0][0]
    #先将第一行第一列的情况算出来
    #第一行的情况
    for col in range(1,C):
        buff[0][col] = buff[0][col-1]+mat[0][col]
    #第一列的情况
    for row in range(1,R):
        buff[row][0] = buff[row-1][0]+mat[row][0]
    for col in range(1,C):
        for row in range(1,R):
            buff[row][col] = max(buff[row][col-1],buff[row-1][col])+mat[row][col]
    return buff[R-1][C-1]



mat = [[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]
print(GetMax(mat))
