#!/usr/bin/env python
#若需按照倒序打印，只需按照列表的倒序打印的方法即可
def PrintChain(head):
    num = []
    node = head
    while node:
        num.append(node)
        node = node._next
    return num[::-1]
print(PrintChain(chainTable.head))
