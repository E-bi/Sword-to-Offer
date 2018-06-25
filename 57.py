def FindNumbersWithSum(s,total):
    for i in range(len(s)):
        tar = total - s[i]
        if tar in s[i+1:]:
            return s[i],tar

s=[1,2,4,67,11,15]
total = 15
print(FindNumbersWithSum(s, total))
