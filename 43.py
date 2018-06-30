def count1(num):
    count = 0
    for i in range(num):
        i = str(i)
        list_i = list(i)
        count_1 = list_i.count('1')
        count = count + count_1
    return count
num = 2123
print(count1(num+1))
