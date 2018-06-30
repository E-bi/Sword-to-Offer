num = 0
print(ord('8')-ord('0'))
news = '123'
for char in news:
    num *= 10
    num += (ord(char)-ord('0'))
    print(num)
