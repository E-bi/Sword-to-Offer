def Fisrt1(s):
    for i in range(len(s)):
        if s[i] not in s[i+1:]:
            return s[i]

s = 'abcdefgheighkldiejdabc'
print(Fisrt1(s))

