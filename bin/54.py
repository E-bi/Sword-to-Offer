class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self,data):
        return self.data
class Tree:
    def __init__(self):
        self.root = None
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
    def inOrder(self,root):
        if not root:
            return []
        result = [root.data]
        left_data = self.inOrder(root.left)
        right_data = self.inOrder(root.right)
        return left_data + result + right_data
def KthNode(root,k):
    k = k-1
    result = tree.inOrder(tree.root)
    return result[k]

tree = Tree()
tree.Add(5)
tree.Add(3)
tree.Add(7)
tree.Add(2)
tree.Add(4)
tree.Add(6)
tree.Add(8)
print(KthNode(tree.root,3))
