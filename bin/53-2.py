a=[0, 2, 3, 4, 5,6, 7, 8, 9, 10]

def findele(a):
    left = 0
    right = len(a)
    flag = False
    for i in range(len(a)):
        if a[i] != i:
            return i
    
right = findele(a)
print(right)

