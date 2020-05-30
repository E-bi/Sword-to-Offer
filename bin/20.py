def isNum(s):
    index = 0
    if s[0] == '+' or s[0] == '-':
        index += 1
        buff = index
        index = scanNum(s, index)
        if index == len(s):
            return True
        elif index != buff: #如果+—号后面是数字（即index更改）
            if s[index] == '.': #如果数字后是小数点
                buff = index
                index = scanNum(s, index) 
                if index != buff: #如果小数点后有数字
                    if s[index] == 'E' or s[index] == 'e':  #如果小数点后有数字，且其中有E或者e
                        index += 1
                        if s[index] == '+' or s[index] == '-': #如果E前面有+-号，则说明后面必须是数字
                            index = scanNum(s, index)
                            if index == len(s)-1:
                                return True
                            else:
                                return False
                        else: #E前面没有+-号，怎说明E后面必须是数字
                            index = scanNum(s, index)
                            if index == len(s)-1:
                                return True
                            else:
                                return False
                    elif index == len(s)-1: #如果小数点后是数字，而且全部都是数字
                            return True
                    else:
                        return False
                elif s[index+1] == 'E' or s[index+1] == 'e':  #如果小数点后直接是E
                    index += 2
                    if s[index] == '+' or s[index] == '-':
                        index = scanNum(s, index)
                        if index == len(s)-1:
                            return True
                        else:
                            return False
                    else:
                        index = scanNum(s, index)
                        if index == len(s):
                            return True
                        else:
                            return False
                else: #如果小数点后既不是e也不是数字
                        return False
            elif s[index] == 'E' or s[index] == 'e': #如果数字后是e
                index += 1
                if s[index] == '+' or s[index] == '-':
                    index += 1
                    index = scanNum(s, index)
                    if index == len(s):
                        return True
                    else:
                        return False
                else:
                    index = scanNum(s, index)
                    if index == len(s):
                        return True
                    else:
                        return False
            else:
                return False
        elif s[index] =='.': #如果+—号后面是小数点
            index += 1
            buff = index
            index = scanNum(s, index) 
            if index == len(s):
                return True
            elif index != buff: #如果小数点后有数字
                if s[index] == 'E' or s[index] == 'e':  #如果小数点后有数字，且其中有E或者e
                    index += 1
                    if s[index] == '+' or s[index] == '-':
                        index = scanNum(s, index)
                        if index == len(s):
                            return True
                        else:
                            return False
                    else:
                        index = scanNum(s, index)
                        if index == len(s):
                            return True
                        else:
                            return False
                if index == len(s): #如果小数点后是数字，而且全部都是数字
                    return True
            elif s[index+1] == 'E' or s[index+1] == 'e':  #如果小数点后直接是E
                index += 2
                if s[index] == '+' or s[index] == '-':
                    index = scanNum(s, index)
                    if index == len(s)-1:
                        return True
                    else:
                        return False
                else:
                    index = scanNum(s, index)
                    if index == len(s)-1:
                        return True
                    else:
                        return False
            else: #如果小数点后既不是e也不是数字
                return False
        else:
            return False
    elif s[0] =='.': #如果开始为小数点
        print(2,'here')
        index += 1
        buff = index
        index = scanNum(s, index) 
        if index != buff: #如果小数点后有数字
            if s[index] == 'E' or s[index] == 'e':  #如果小数点后有数字，且其中有E或者e
                index += 1
                if s[index] == '+' or s[index] == '-':
                    index = scanNum(s, index)
                    if index == len(s):
                        return True
                    else:
                        return False
                else:
                    index = scanNum(s, index)
                    if index == len(s):
                        return True
                    else:
                        return False
            if index == len(s)-1: #如果小数点后是数字，而且全部都是数字
                return True
        elif s[index+1] == 'E' or s[index+1] == 'e':  #如果小数点后直接是E
            index += 2
            if s[index] == '+' or s[index] == '-':
                index = scanNum(s, index)
                if index == len(s):
                    return True
                else:
                    return False
            else:
                index = scanNum(s, index)
                if index == len(s):
                    return True
                else:
                    return False
        else: #如果小数点后既不是e也不是数字
            return False
    elif s[0] in num_list: #如果开始为数字    
        index = scanNum(s, index)
        if index == len(s):
            return True
        elif s[index] == '.': #如果数字后是小数点
            index += 1
            buff = index
            index = scanNum(s, index) 
            if index != buff: #如果小数点后有数字
                if index == len(s):#如果小数点后是数字，而且全部都是数字
                    return True
                elif s[index] == 'E' or s[index] == 'e':  #如果小数点后有数字，且其中有E或者e
                    index += 1
                    if s[index] == '+' or s[index] == '-': #如果E前面有+-号，则说明后面必须是数字
                        index = scanNum(s, index)
                        if index == len(s):
                            return True
                        else:
                            return False
                    else: #E前面没有+-号，怎说明E后面必须是数字
                        index = scanNum(s, index)
                        if index == len(s):
                            return True
                        else:
                            return False
                else:
                    return False
            elif s[index+1] == 'E' or s[index+1] == 'e':  #如果小数点后直接是E
                index += 2
                if s[index] == '+' or s[index] == '-':
                    index = scanNum(s, index)
                    if index == len(s):
                        return True
                    else:
                        return False
                else:
                    index = scanNum(s, index)
                    if index == len(s):
                        return True
                    else:
                        return False
            else: #如果小数点后既不是e也不是数字
                return False
        elif s[index] == 'E' or s[index] == 'e': #如果数字后是e
            index += 1
            if s[index] == '+' or s[index] == '-':
                index = scanNum(s, index)
                if index == len(s):
                    return True
                else:
                    return False
            else:
                index = scanNum(s, index)
                if index == len(s):
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False

def scanNum(s,index):
    print(index)
    while s[index] in num_list:
        index += 1
        if index == len(s):
            break
    return index
num_list = ['1','2','3','4','5','6','7','8','9','0']    
s='1.2.3'
print(s)
print(isNum(s))
