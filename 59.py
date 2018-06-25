def maxInWindow(s,size):
    buff = []
    for i in range(len(s)-size+1):
        FirstInWindow = s[i]
        SecondeInWindow = s[i+1]
        ThirdInWindow = s[i+2]
        maxNum = max(FirstInWindow,SecondeInWindow,ThirdInWindow)
        buff.append(maxNum)
    return buff

s = [2,3,4,2,6,2,5,1]
size = 3
print(maxInWindow(s,size))
