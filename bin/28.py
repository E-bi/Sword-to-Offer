class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
pRoot = TreeNode(pRoot)
def startToJudge(pRoot):
    return isSymmetrical(pRoot,pRoot)
def isSymmetrical(pRoot1,pRoot2):
    if pRoot1 == None and pRoot2 == None:
        return True
    if pRoot1 == None or pRoot2 == None:
        return False
    if pRoot1.data != pRoot2.data:
        return False
    return isSymmetrical(pRoot1.left, pRoot2.right) and isSymmetrical(pRoot1.right, pRoot2.left)
