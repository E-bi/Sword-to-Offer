#矩阵中的路径
def hasPath(path,mat):
    if not mat or not path:
        return 'No mat or path'
    R = len(mat) #行
    C = len(mat[0]) #列
    visited = [[False]*C]*R 
    pathLength = 0
    for row in range(R):
        for col in range(C):
            if hasPathCore(mat,R,C,row,col,path,pathLength,visited):
                return True
    return False
def hasPathCore(mat,R,C,row,col,path,pathLength,visited):
    if pathLength == len(path):
        return True
    hasPath = False
    if (row >= 0) & (row < R) & (col >= 0) & (col< C) & (mat[row][col] == path[pathLength]) & (not visited[row][col]):
        pathLength += 1
        visited[row][col] = True
        hasPath = hasPathCore(mat, R, C,row, col-1, path, pathLength,visited) or hasPathCore(mat, R, C, row-1, col, path, pathLength, visited) or hasPathCore(mat, R, C, row, col+1, path, pathLength, visited) or hasPathCore(mat, R, C, row+1, col,path,pathLength,visited)
        if not hasPath:
            pathLength -= 1
            visited[row][col] = False
    return hasPath


path = 'bfce'
mat = [['a','b','t','g'],['c','f','c','s'],['j','d','e','h']]
print(hasPath(path,mat))
