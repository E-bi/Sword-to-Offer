def Add(num1,num2):
    while num2 != 0:
        sum_num = num1 ^ num2
        carry = (num1 & num2)<<1    
        num1 = sum_num
        num2 = carry
    return num1

num1 = 5
num2 = 17
print(Add(num1,num2))
