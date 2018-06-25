class Node:
    def __init__(self,data,_next = None):
        self.data = data
        self._next = _next
    def __repr__(self):
        return str(self.data)

class ChainTable:
    def __init__(self):
        self.head = None
        self.length = 0
    def isEmpty(self):
        if self.length == 0:
            return True

    def add(self,dataOrnode):
        item = None
        if isinstance(dataOrnode,Node):
            item = dataOrnode
        else:
            item = Node(dataOrnode)
        if not self.head:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1
    def print_Chain(self):
        if self.isEmpty():
            return 'kong'
        else:
            num = []
            node = self.head
            while node:
                num.append(node)
                node = node._next
            return num
    def getItem(self,index):
        if index <= 0:
            return False
        if index > self.length:
            return False
        pHead = 0
        pLast = 0
        j = 0
        node_head = self.head
        node_last = self.head
        while node_head and pHead<self.length-1:
            node_head = node_head._next
            pHead += 1
            if index == 1:
                num = node_head
            elif index !=1 and pHead >= index - 1:
                num = node_last
                node_last = node_last._next
                pLast += 1
        return num

chain = ChainTable()
for i in range(20):
    chain.add(i)

print(chain.print_Chain())
print(chain.getItem(9))
