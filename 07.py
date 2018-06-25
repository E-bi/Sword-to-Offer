#重建二叉树   未完成
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class tree:
    def __init__(self):
        self.root = None
    def find_root(preorder,midorder):
        #前序遍历的第一个数字是根节点的值
        #判断是不是长度为1的
        self.add(FirstRoot)
        self.add()
        midorder_left = midorder[:FirstRoot_index_in_midorder]
        find_root(preorder,midorder_left)
        midorder_right = midorder[FirstRoot_index_in_midorder+1:]
        find_root(preorder,midorder_right)
    def add(self,dataOrNode):
        if isinstance(dataOrNode,Node):
            node = dataOrNode
        else:
            node = Node(dataOrNode)
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
    def construct(preorder,midorder):
        left_tree = 0
        q=[]
        FirstRoot = preorder[left_tree]
        q.append(FirstRoot)
        self.add(FirstRoot)
        while True:       
            FirstRoot_index_in_midorder = midorder.index(FirstRoot)
            #将midorder按照FirstRoot分为左右子树
            midorder_left = midorder[:FirstRoot_index_in_midorder]
            left_tree = len(FirstRoot_index_in_midorder)
            q.append(left_tree)
            midorder_right = midorder[FirstRoot_index_in_midorder+1:] 
            right_tree = len(midorder_right)
preorder = [1,2,4,7,3,5,6,8]
midorder = [4,7,2,1,5,3,8,6]
len_preorder = len(preorder)
if len_preorder ==1:
    Root = preorder[0]
    return Root
if len_preorder == 0:
    return '输入无效'
else:
    FirstRoot = preorder[0]
    construct(preorder,midorder)
