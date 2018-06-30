def Permutation(string,i):  
    if string == None:  
        return  
    if string[i] == '\n':  
        print(''.join(string[:i]))  
    else:  
        for j in range(i,len(string)-1):              
            string[j],string[i] = string[i],string[j] #将前面的字符依次与后面进行交换 
            Permutation(string,i+1)  
            string[j],string[i] = string[i],string[j]  #固定第一个字母对交换完成后的后面的数组进行排列
s = 'abc'
string = list(s+'\n')
Permutation(string,0) 
