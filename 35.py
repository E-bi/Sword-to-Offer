class ComplexNode:
    def __init__(self,data,m_pNext= None, m_pSibling= None):
        self.data = data
        self.m_pNext = m_pNext
        self.m_pSibling = m_pSibling

class pHead(ComplexNode):
    pass
def ComplexListNodeClone(pHead):

