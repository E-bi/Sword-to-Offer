def maxInWindow(s,size):
    buff = []
    for i in range(len(s)-size+1):
        new_s = s[i:size+i]
        maxNum = max(new_s)
        buff.append(maxNum)
    return buff

s = [2,3,4,2,6,2,5,1]
size = 2
print(maxInWindow(s,size))
