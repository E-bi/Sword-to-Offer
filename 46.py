def ProcessTranslationCount(number):
    if number < 0 :
        return 0
    numberInString = str(number)
    return GetTranslationCount(numberInString)

def GetTranslationCount(numberInString):
    length = len(numberInString)
    counts = [length]
    count = 0
    for i in range(length-1,-1,-1):
        if i == length-1:
            count = 1
        if i < length-1:
            digit1 = ord(numberInString[i])-ord('0')
            digit2 = ord(numberInString[i+1])- ord('0')
            converted = digit1*10+digit2
            if converted >= 10 & converted <= 25:
                if i <length-2:
                    count += counts[i+2]
                else:
                    count += 2
            else:
                count += 1
        counts[i] = count
    count = counts[0]
    return count
num = 12258
ProcessTranslationCount(num)
