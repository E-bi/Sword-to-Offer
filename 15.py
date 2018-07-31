#方法1
def find_1(num):
    len_num = 65 #若不设定左移次数，系统将一直左移
    times = 0
    count = 0
    pat =1
    while times <= len_num+1:
        #如果最后一位是1：
        if num&pat:
           count += 1
        pat = pat << 1
        times = times+1
    return count
#方法2
def find_12(num):
    count = 0
    while num:
        count += 1
        num = (num-1)&num
    return  count


print(find_1(123))
print(find_12(123))
