def GetNumberSameIndex(s):
    for i in range(len(s)):
        if i == s[i]:
            return i

s=[-3,-3,1,3,5]
print(GetNumberSameIndex(s))
