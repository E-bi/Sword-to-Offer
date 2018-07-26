def left_rotate(a):
    num = 2
    buff = []
    for i in range(num):
        buff.append(a[i])
    b = ''.join(buff)
    c = a[num:]
    return b+c
a = "abcdefg"
print(left_rotate(a))
