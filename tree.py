#创建节点类
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
#创建树类
class tree:
    def __init__(self):
        self.root = None
    def add(self,data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def traverse(self): #层次遍历/宽度优先遍历
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.data]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.data)
            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.data)
        return res
    def preorder(self,root): #前序遍历
        if root is None:
            return []
        result = [root.data]
        left_data = self.preorder(root.left)
        right_data = self.preorder(root.right)
        return result + left_data + right_data
    def inorder(self,root):  #中序遍历
        if root is None:
            return []
        result = [root.data]
        left_data = self.inorder(root.left)
        right_data = self.inorder(root.right)
        return left_data + result + right_data
    def postorder(self,root):  #后序遍历
        if root is None:
            return []
        result = [root.data]
        left_data = self.postorder(root.left)
        right_data = self.postorder(root.right)
        return left_data + result + right_data
t= tree()
for i in range(10):
    t.add(i)
print('层序遍历:',t.traverse())
print('先序遍历:',t.preorder(t.root))
print('中序遍历:',t.inorder(t.root))
print('后序遍历:',t.postorder(t.root))

基金会
