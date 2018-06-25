def FindNumsAppearOnce(s):
    s.sort()
    for i in range(0,len(s)-1,3):
        if s[i] != s[i+1]:
            return s[i]




s = [2,3,3,3,2,2,4,4,4,1,5,5,5]
print(FindNumsAppearOnce(s))
