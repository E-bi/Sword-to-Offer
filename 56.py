def FindNumsAppearOnce(s):
    list_s = list(set(s))
    for i in range(0,len(s)):
        if s[i] in s[i+1:]:
            list_s.remove(s[i])
    return list_s



s = [2,4,3,6,3,2,5,5]
print(FindNumsAppearOnce(s))
