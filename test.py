def FindMaxSum(a):
    len_a = len(a)
    buff = []
    total = 0
    for i in range(len_a):
        total = total+a[i]
        if total<a[i]:
            buff.append(total)
            total = a[i]
    print(max(buff))
a= [1,-2,3,10,-4,7,2,-5]
FindMaxSum(a)
