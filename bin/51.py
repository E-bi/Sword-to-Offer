def ReverseNum(s):
    buff = []
    for i in range(len(s)):
        new_s = s[i+1:]
        for j in range(len(new_s)):
            buff += [[s[i],new_s[j]]]
    return buff
s = [7,6,5,4,9]
s.sort(reverse=True)

print(ReverseNum(s))
