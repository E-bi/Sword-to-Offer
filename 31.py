def IsPopOrder(l1, l2):
    stack = []
    while l1:
        stack.append(l1[-1])
        l1.pop()
    while l2:
        if stack.pop() != l2.pop():
            return False
        else:
            return True
    return False
l1 = [1,2,3,4,5]
l2 = [5,4,3,2,1]
print(IsPopOrder(l1, l2))
