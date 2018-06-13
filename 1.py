#输入字符串，打印字符串的所有排列
stra = 'aaa'
def choose(stra):
    buff_s = []
    n = len(stra)
    if n:
        return False
    if n == 1:
        return stra
    if n == 2 and stra[0] != stra[1]:
        buff = []
        str_1 = ''.join([str[0],stra[1]])
        buff.append(str_1)
        str_2 = ''.join([str[1],stra[0]])
        buff.append(str_2)
        return buff
    else:
        for cha in stra:
            buff_s.append(cha)
            stra.remove(cha)
            tar = choose(stra)
            buff_s.append(tar)
    return buff_s
buff_s = choose(stra)
print(buff_s)
