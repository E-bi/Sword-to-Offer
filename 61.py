def IsContinuous(numbers):
    if not numbers:
        return None
    numbers.sort()
    #若其中有对子则返回
    for i in range(len(numbers)-1):
        if numbers[i] in numbers[i+1:] and numbers[i] != 0:
            return
    count_0 = 0
    count_inter = 0
    #找出数组中0的个数
    for num in numbers:
        if num == 0:
            count_0 += 1
    #找出数组中空缺的间隔
    for i in range(count_0+1,len(numbers)-1):
        count_inter += numbers[i+1]-numbers[i]-1
    return count_inter <= count_0
numbers = [0,2,3,5,6]
print(IsContinuous(numbers))
