class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    def Add(self,num):
        node = TreeNode(num)
        if not self.root:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if not pop_node.left:
                    pop_node.left = node
                    return
                if not pop_node.right:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

def FindPath(Atree, tar, path, currentSum):
    if not Atree:
        return False
    Root = Atree.root
    currentSum += Root.data
    path.append(Atree.root)
    #如果是叶节点，并且路径上节点的值的和等于输入的值
    #则打印这条路径
    if (not Root.left) & (not Root.right):
        isLeaf = True
    else:
        isLeaf = False
    if currentSum == tar & isLeaf:
        print("A path is found:")
        print(path)
    #如果不是叶节点，则遍历它的子节点
    if Root.left:
        FindPath(Root.left, tar, path, currentSum)
    if Root.right:
        FindPath(Root.left, tar, path, currentSum)
    path.pop()

Atree = Tree()
Atree.Add(10)
Atree.Add(5)
Atree.Add(12)
Atree.Add(4)
Atree.Add(7)

#找路径
tar = 22
currentSum = 0
path = []
FindPath(Atree, tar, path, currentSum)
