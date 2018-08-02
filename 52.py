class ListNode:
    def __init__(self,data,_next=None):
        self.data =data
        self._next = _next
    def __repr__(self):
        return str(self.data)
def findSame(Head1,Head2):
    longNode = Head1
    shortNode = Head2
    length1 = getLengthOfNode(Head1)
    length2 = getLengthOfNode(Head2)
    dif = length1 - length2
    if length2 > length1:
        longNode = Head2
        shortNode = Head1
        dif = -dif
    for i in range(dif):
        longNode = longNode._next
    while longNode and shortNode:
        if longNode.data == shortNode.data:
            return longNode
        longNode = longNode._next
        shortNode = shortNode._next
def getLengthOfNode(head):
    length = 0
    while head:
        length += 1
        head = head._next
    return length

