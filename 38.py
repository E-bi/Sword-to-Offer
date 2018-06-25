def Permutation(string,i):  
    if string == None:  
        return  
    if string[i] == '\n':  
        print("%s"%''.join(string[:i]))  
    else:  
        for j in range(i,len(string)-1):              
            string[j],string[i] = string[i],string[j]  
            Permutation(string,i+1)  
            string[j],string[i] = string[i],string[j]  
s = 'abcdefg'
string = list(s+'\n')
Permutation(string,0) 
