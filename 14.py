def max_product(length):
    if length <= 1:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    products = []
    products.append(0)
    products.append(1)
    products.append(2)
    products.append(3)
    for i in range(4,length+1):
        max_num = 0
        for j in range(1,i//2+1):
            product = products[j]*products[i-j]
            if max_num < product:
                max_num = product
        products.append(max_num)
    max_num = products[length]
    return max_num

print(max_product(8))
