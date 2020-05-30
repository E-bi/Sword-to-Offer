class Node:
    def __init__(self,data,_next = None):
        self.data = data
        self._next = _next
    def __repr__(self):
        return str(self.data)

def ChainTable(Head,index):
    num = []
    root = Head
    while root:
        num.append(root)
        root = root._next
    if index > len(num):
        return False
    else:
        return num[-index]
