'''
class Factorial:
    def __init__(self):
        self.cache = {}
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[n] = 1
            else:
                self.cache[n] = n * self.__call__(n-1)
        return self.cache[n]

fact = Factorial()  
for i in range(10):                                                             
    print("{}! = {}".format(i, fact(i)))

class decorator(object):
    def __init__(self, name):
        self.name = name
        print('传来的参数是：',self.name)
    def __call__(self, func):
        print('到我call的地盘了')
        print('传来的参数是：',func)
        def inner(*args, **kwargs):
            print('{}'.format(*args, **kwargs))
            return func(*args, **kwargs)
        return inner

@decorator('parm')
def param_check(b):
    print('Hello'+' '+b)
b = 'world'
param_check(b)
'''

class decorator(object):
    def __init__(self,name):
        self.name = name
        print('传来的参数是：',self.name)
    def __call__(self, func):
        print('到我call的地盘了')
        print('传来的参数是：',func)
        def inner():
            func()
        return inner

@decorator('parm')  
def param_check():
    print('Hello')
param_check()
