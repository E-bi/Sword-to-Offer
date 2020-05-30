class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = Noneo
    def Add(self,data):
        node = TreeNode(data)
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
def Find_Depth(root):
    if not root:
        return 0
    nLeft = Find_Depth(root.left)
    nRight = Find_Depth(root.right) 
    return nLeft+1 if nLeft> nRight else nRight+1


tree = Tree()
tree.Add(5)
tree.Add(3)
tree.Add(7)
tree.Add(2)
tree.Add(4)
tree.Add(6)
tree.Add(8)
print(Find_Depth(tree.root))
