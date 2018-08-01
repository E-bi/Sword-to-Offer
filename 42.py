def FindMaxSum(a):
    len_a = len(a)
    maxnum = 0
    total = 0
    for i in range(len_a):
        total = total+a[i]
        if maxnum <= total:
            maxnum = total
        if total<a[i]:
            total = a[i]
            maxnum = a[i]
    print(maxnum)
a= [1,-2,3,10,-4,7,2,-5]
FindMaxSum(a)
