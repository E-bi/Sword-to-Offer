#!/usr/bin/env python
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


Preorder = [1,2,4,7,3,5,6,8] #前序遍历
Inorder = [4,7,2,1,5,3,8,6] #中序遍历
def ConstructCore(Preorder,Inorder):
    rootValue = Preorder[0]
    rootInorder = 0
    root = Node()
    root.data = rootValue
    root.right = None
    root.left = None
    #在中序遍历中找到根节点的值
    while rootInorder < len(Inorder) & Inorder[rootInorder] != rootValue:
        rootInorder += 1 #求出在中序遍历中根节点出现的位置的长度
    if rootInorder == len(Inorder):
        raise Exception("Invalid Input")
    leftLength = rootInorder #左子树的长度
    leftPreorderEnd = leftLength #在前序遍历中左子树结束的位置
    if leftLength > 0 :
        root.left = ConstructCore(Preorder[1:leftLength+1],Inorder[0])
