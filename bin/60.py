g_maxValue = 6
def PrintProbablity(number):
    if number<1:
        return
    pProbablities = [0]*2
    pProbablities[0] = g_maxValue * number + 1
    pProbablities[1] = g_maxValue * number + 1
    for i in range(g_maxValue):
        pProbablities[0][i] = 0
        pProbablities[1][i] = 0
    flag = 0
    for i in range(1,g_maxValue+1):
        pProbablities[flag][i] = 1
    for k in range(2,number+1):
        for i in range(k):
            pProbablities[1 - flag][i] = 0
        for i in range(k,g_maxValue+1):
            pProbablities[1-flag][i] = 0
            for j in range(1,min(i,g_maxValue)+1):
                pProbablities[1-flag][i] += pProbablities[flag][i-j]
        flag = 1-flag
    total = pow(g_maxValue,number)
    for i in range(number,g_maxValue):
        ratio = pProbablities[flag][i]/total
        print(i,ratio)
PrintProbablity(1)
