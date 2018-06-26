class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
pRoot1 = TreeNode(pRoot1)
pRoot2 = TreeNode(pRoot2)
def HasSubtree(pRoot1,pRoot2):
    result = False
    if pRoot1 != None & pRoot2 != None:
        if pRoot1.data == pRoot2.data:
            result = DoesTree1HaveTree2(pRoot1,pRoot2)
        if != result:
            result = HasSubtree(pRoot1.left, pRoot2)
        if != result:
            result = HasSubtree(pRoot1.right, pRoot2)
    return result

def DoesTree1HaveTree2(pRoot1,pRoot2):
    if pRoot2 == None:
        return True
    if pRoot1 == None:
        return False
    if pRoot1.data != pRoot2.data:
        return False
    return DoesTree1HaveTree2(pRoot1.left,pRoot2.left) & DoesTree1HaveTree2(pRoot1.right,pRoot2.right)
