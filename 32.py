class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Tree(object):
    def __init__(self):
        self.root = None
    def add(self,num):
        node = TreeNode(num)
        if self.root == None:
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
    def traverse(self):
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

    def print_inline(self):
        '''
        分行从上到下打印二叉树
        '''
        if self.root == None:
            return None
        q = [self.root]
        next_level = 0 #下一层的节点数
        toBePrinted = 1 
        while q != []:
            pop_node = q.pop(0)
            print(pop_node.data,end=" ")
            if pop_node.left != None:
                q.append(pop_node.left)
                next_level += 1
            if pop_node.right != None:
                q.append(pop_node.right)
                next_level += 1
            toBePrinted -= 1
            if toBePrinted == 0:
                print("\n")
                toBePrinted = next_level
                next_level = 0

    def PrintInZ(self):
        '''
        z字形打印二叉树
        '''
        if self.root == None:
            return None
        levels = [[],[]]
        current = 0
        next_next = 1
        levels[current].append(self.root)
        while levels[0] or levels[1]:
            pNode = levels[current].pop()
            print(pNode.data,end=',')
            if current == 0:
                if pNode.left:
                    levels[next_next].append(pNode.left)
                if pNode.right:
                    levels[next_next].append(pNode.right)
            else:
                if pNode.right:
                    levels[next_next].append(pNode.right)
                if pNode.left:
                    levels[next_next].append(pNode.left)
            if not levels[current]:
                print("\n")
                current = 1-current
                next_next = 1- next_next
tree = Tree()
tree.add(8)
tree.add(6)
tree.add(10)
tree.add(5)
tree.add(7)
tree.add(9)
tree.add(11)
print(tree.traverse())
tree.print_inline()
tree.PrintInZ()

