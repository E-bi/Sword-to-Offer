class Node:
    def __init__(self,data,_next = None):
        self.data = data
        self._next = _next
    def __repr__(self):
        '''
        用来定义Node的字节输出
        '''
        return str(self.data)
def Merge(pHead1,pHead2):
    if pHead1 == None:
        return pHead2
    elif pHead2 == None:
        return pHead1
    pMergedHead = None
    if pHead1._next < pHead2._next:
        pMergedHead = pHead1
        pMergedHead._next = Merge(pHead1._next,pHead2._next)
    else:
        pMergedHead = pHead2
        pMergedHead._next = Merge(pHead1._next, pHead2._next)
    return pMergedHead

