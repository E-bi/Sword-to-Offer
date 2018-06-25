#青蛙跳台阶问题
def stage(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        met1 = 1
        met2 = 2
        for i in range(n-2):
            met3 = met1 + met2
            met1 = met2
            met2 = met3
        return met3
print(stage(10))
