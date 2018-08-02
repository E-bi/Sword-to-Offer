def left_rotate(a,num):
    buff = []
    for i in range(num):
        buff.append(a[i])
    b = ''.join(buff)
    c = a[num:]
    return c+b
a = "abcdefg"
print(left_rotate(a,2))
