#若需按照倒序打印，只需按照列表的倒序打印的方法即可

class Node:
    def __init__(self, val, _next=None):
        self.val = val
        self._next = _next

def Construct():
    Head = Node(0)
    L = Head
    for i in range(1, 20):
        L._next = Node(i)
        L = L._next
    return Head


def PrintChain(head):
    num = []
    node = head
    while node:
        num.append(node.val)
        node = node._next
    return num[::-1]

Head = Construct()
print(PrintChain(Head))
