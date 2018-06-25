def GetUglyNumber(number):
    while number %2 == 0:
        number = number/2
    while number %3 == 0:
        number = number/3
    while number %5 == 0:
        number = number/3
    return number==1
count = 1500
for i in range(1,count+1):
    if GetUglyNumber(i):
        print(i)
