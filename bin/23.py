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
#判断是否有环
def MeetingNode(pHead):
    if pHead == None:
        return None
    pSlow = pHead._next
    if pSlow == None:
        return None
    pFast = pSlow._next
    while pFast != None and pSlow != None:
        if pSlow == pFast:
            return pFast
        pSlow = pSlow._next
        pFast = pFast._next
        if pFast != None:
            pFast = pFast._next
    return None

def EntryNodeOfLoop(pHead):
    meetingNode = MeetingNode(pHead)
    if meetingNode == None:
        return None
    #得到环中节点的数目
    nodesInLoop = 1
    pNode1 = meetingNode
    while pNode1._next != meetingNode:
        pNode1 = pNode1._next
        nodesInLoop += 1
    #先移动pNode1，次数为环中节点的数目
    pNode1 = pHead
    for i in range(nodesInLoop):
        pNode1 = pNode1._next
    #再移动pNode1和pNodes2
    pNode2 = pHead
    while pNode1 != pNode2:
        pNode1 = pNode1._next
        pNode2 = pNode2._next
    return pNode1
