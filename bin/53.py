def CountNum(s,tar):
    s.sort()
    count = 0
    for cha in s:
        if cha == tar:
            count += 1
    return count
s=[1,2,3,4,5,3,2,3,2,3,2,33,2]
tar = 3
print(CountNum(s,tar))
