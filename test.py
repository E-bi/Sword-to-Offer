a='abcd efg'
a=list(a)
for i in range(len(a)):
    if a[i] == ' ':
        a.insert(i,'%20')
print(a)
