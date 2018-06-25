def ProcessTranslationCount(number):
    if number < 0 :
        return 0
    numberInString = str(number)
    return GetTranslationCount(numberInString)

def GetTranslationCount(numberInString):
    length = len(numberInString)
    counts = length
    count = 0
    for i in range(length-1,-1,-1):
        count = 0
        if i < length - 1:
            count = counts[i+1]
        else:
            count = 1
        if i < length-1:
            digit1 = numberInString[i]-'0'
            digit2 = numberInString[i+1]-'0'
            converted = digit1*10+digit2
            if converted >= 10 & converted <= 25:
                if i <length-2:
                    count += counts[i+2]
                else:
                    count += 1
        counts[i] = count
    count = counts[0]
    return count
