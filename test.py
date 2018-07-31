def isNum(s):
    numList = ['1','2','3','4','5','6','7','8','9','0']
    if s.startswith('+') or s.startswith('-'):
        s.pop(0)
    elif s.startswith('.'):
        s.pop(0)
    else:
        if s[0] not in numList:
            return False
        while s[0] in numList:
            s.pop(0)
        if s.startswith('.'):
            s.pop(0)
