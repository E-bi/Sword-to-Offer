a = "abcdefg"
num = 2
buff = []
for i in range(num):
    buff.append(a[i])
b = ''.join(buff)
c = a[num:]
print(c+b)