def MaxDiff(s):
    MaxNum = s[0]
    buff_num = []
    for i in range(1,len(s)):
        minNum = min(s[:i])
        MaxNum = s[i] - minNum
        buff_num.append(MaxNum)
    Big = max(buff_num)
    return Big

s = [9,11,8,5,7,12,16,14] 
print(MaxDiff(s))
