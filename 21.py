def find_odd(num):
    len_num = len(num)
    if len_num <= 1:
        return num
    else:
        #初始化左右指针的位置
        left = 0
        right = len_num-1
        while True:
            if left >= right:
                return num
            #如果左边是偶数而右边是奇数
            elif isOdd(num[left]) and not isOdd(num[right]):
                #交换两边的数字
                num[left],num[right] = num[right],num[left]
                #左边向右移一位
                left += 1
                #右边向左移一位
                right -= 1
            #如果左边是奇数，右边是偶数
            elif not isOdd(num[left]) and isOdd(num[right]):
                #右边向左移一位
                right -= 1
                #左边向右移一位
                left += 1
            #如果两边都是奇数
            elif not isOdd(num[left]) and not isOdd(num[right]):
                left += 1
            #如果两边都是偶数
            elif isOdd(num[left]) and isOdd(num[right]):
                #右边向左移一位
                right -= 1
                


def isOdd(n):
    if n%2 == 0:
        return True
    else:
        return False

num = [2,2,2,2,2,2,2,1]
result = find_odd(num)
print(result)
