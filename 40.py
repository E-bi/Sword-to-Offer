def GetLastNumbers(a,k):
    a.sort()
    n = len(a)
    if n == 0:
        print(None)
    elif k <= 0:
        print('k<=0')
    elif k>=n:
        print(a)
    else:
        for i in range(k):
            print(a[i])
a=[1,2,3,4,3,2,3,4,3,4,5,6]
GetLastNumbers(a,3)
