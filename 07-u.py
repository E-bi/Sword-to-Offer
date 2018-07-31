#!/usr/bin/env python
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


Preorder = [1,2,4,7,3,5,6,8] #前序遍历
Inorder = [4,7,2,1,5,3,8,6] #中序遍历
def ConstructCore(Preorder,Inorder):
    if len(Preorder) == 0:
        return None
    if len(Preorder) == 1:
        return TreeNode(Preorder[0])
    else:
        root = TreeNode(Preorder[0])
        root.left = ConstructCore(Preorder[1:Inorder[Inorder.index(Preorder[0])+1]],Inorder[:Inorder.index(Preorder[0])])
        root.right = ConstructCore(Preorder[Inorder.index(Preorder[0])+1:],Inorder[Inorder.index(Preorder[0])+1:])
    return root
