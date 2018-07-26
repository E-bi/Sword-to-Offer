def IsNum(char):
    tar = ['1','2','3','4','5','6','7','8','9','0']
    return char in tar
def StrToInt(s):
    if not s:
        return
    isPlus = True
    num = 0
    if s.startswith('-'):
        isPlus = False
        news = s[1:]
    elif s.startswith('+'):
        news = s[1:]
    else:
        news = s[::]
    try:
        for char in news:
            if IsNum(char):
                num *= 10
                num += ord(char)-ord('0')
            else:
                print('Invalid Input')
                return 
        if isPlus:
            print(num)
        else:
            print(-num)
    except:
        print('Invalid Input')
StrToInt('110')
            

