def longestSubstring(string):
    start = string[0]
    buff = []
    buff.append(start)
    tar = []
    for char in string[1:]:
        if char not in buff:
            buff.append(char)
            buff1 = ''.join(buff)
        else:
            tar = tar+[buff1]
            buff = []
            buff.append(char)
    tar = tar+[buff1]
    max_index = 0
    for index in range(len(tar)):
        if len(tar[index])>len(tar[max_index]):
            max_index = index
    return tar[max_index]
string = 'arabcacfr'
print(longestSubstring(string))
