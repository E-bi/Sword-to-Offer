def longestSubstring(string):
    tar_dict = {}
    buff = ''
    count = 0
    for char in string:
        if char in buff:
            tar_dict[buff] = count
            count = 1
            buff = char
        else:
            buff += char
            count += 1
    tar_dict[buff] = count
    tar = sorted(tar_dict.items(),key=lambda x:x[1],reverse=True)
    return tar[0][0]
string = 'arabcacfr'
print(longestSubstring(string))
