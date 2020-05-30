#定义节点类
class Node:
    def __init__(self,data,_next = None):
        self.data = data
        self._next = _next
    def __repr__(self):
        '''
        用来定义Node的字节输出
        '''
        return str(self.data)    

class ChainTable:
    def __init__(self):
        self.head = None
        self.length = 0
    def isEmpty(self):
        return(self.length == 0)

    def add(self,dataOrNode):
        item = None
        if isinstance(dataOrNode,Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        if not self.head: #若头结点为空，则加入头结点
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._next: #如果节点的next存在，则要将下一个节点的数赋予节点
                node = node._next
            node._next = item #如果节点的next不存在，将本节点的next赋予节点
            self.length += 1


        def delete(self,index):
            if self.isEmpty():
                return False #if ChainTable is empty then return False
            if index <0 or index >length:
                print('超出索引长度')
                return
            if index == 0:
                self.head = self.head._next
                self.length -= 1
                return 
            j = 0
            '''
            prenode用来定义前导节点
            node用来定义当前结点
            '''
            prenode = self.head
            node = self.head 
            while node._next and j < index:#当下一个节点存在，且j小于index
                prenode = node
                node = node._next
                j += 1
            if j == index:
                prenode._next = node._next#将当前节点的前导节点替换为当前节点的下一个节点的前导节点，
                #即相当于将当前节点删除
    def PrintChain(self):
        if self.isEmpty():
            print('ChainTable is None')
            return
        num = []
        node = self.head
        while node:
            num.append(node)
            node = node._next
        return num
def delete(Head,index):
    if index <0 or index >length:
        print('超出索引长度')
        return
    if index == 0:
        Head = Head._next
        return 
    j = 0
    '''
    prenode用来定义前导节点
    node用来定义当前结点
    '''
    prenode = Head
    node = Head 
    while node._next and j < index:#当下一个节点存在，且j小于index
        prenode = node
        node = node._next
        j += 1
    if j == index:
        prenode._next = node._next#将当前节点的前导节点替换为当前节点的下一个节点的前导节点，
        #即相当于将当前节点删除

Chain = ChainTable()
for i in range(5):
    Chain.add(i)
print(Chain.PrintChain())
