class Node:
    def __init__(self,data,_next = None):
        self.data = data
        self._next = _next
    def __repr__(self):
        '''
        用来定义Node的字节输出
        '''
        return str(self.data)
pHead = Node(pHead)
def ReverseList(pHead):
    pReverseHead = None
    pNode = pHead
    pPrev = None
    while pNode != None:
        pNext = pNode._next
        if pNext == None:
            pReverseHead = pNode
        pNode._next = pPrev
        pPrev = pNode
        pNode = pNext
    return pReverseHead
