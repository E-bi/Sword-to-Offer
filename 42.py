a= [1,-2,3,10,-4,7,2,-5]
len_a = len(a)
max = 0
total = 0
for i in range(len_a):
    total = total+a[i]
    if max <= total:
        max = total
    if total<a[i]:
        total = a[i]
        max = a[i]
print(max)
