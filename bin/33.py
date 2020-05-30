def VerifySequenceOfBST(s):
    if s is None:
        return False
    root = s[-1]
    #在二叉搜索树中左子树节点的值小于根节点的值
    for i in range(len(s)):
        if s[i] > root:
            break
    #在二叉搜索树中右子树节点的值大于根节点的值
    for j in range(i,len(s)):
        if s[j] < root:
            return False
    #利用递归判断左子树是不是符合二叉搜索树
    left = True
    if i>0:
        left = VerifySequenceOfBST(s[:i])
    #利用递归判断右子树是不是符合二叉搜索树
    right = True
    if i < len(s)-1:
        right = VerifySequenceOfBST(s[i:len(s)-1])
    return left&right





s = [5,6,7,9,11,10,8]
s = [7,4,6,5]
print(VerifySquenceOfBST(s))
