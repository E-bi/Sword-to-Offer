def FindContinuousSequence(s):
    total = 0
    buff = []
    start = 1
    while start:
        if start == s:
            return buff
        for i in range(start,s):
            total = total + i
            if total == s:
                total = 0
                seq = str(start)+'~'+str(i)
                start = start + 1
                buff.append(seq) 
            elif i == s-1:
                total = 0
                start = start + 1

s = 15
print(FindContinuousSequence(s))
