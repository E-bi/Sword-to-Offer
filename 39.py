def MoreThanHalfNum(a):
    a.sort()
    len_a = len(a)
    if len_a == 0:
        print(None)
    elif len_a == 1:
        print(a[0])
    else:
        tar = len_a/2
        start = a[0]
        count = 1
        for num in a[1:]:
            if num == start:
                count +=1
                if count>tar:
                    print(num)
                    break
            else:
                count = 1
                start = num
a = [1,2,3,4,2,3,2,2,4,3,2,3,2,2,2,2,2,2,2,2,2,2]
MoreThanHalfNum(a)
