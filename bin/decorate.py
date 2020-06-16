def lowerWord(word='Hi There'):
    return word.lower()

from functools import wraps
def start_word_upper(func):
    @wraps(func)
    def inner(*args,**kwargs):
        word = func(*args,**kwargs)
        return word.captialize()
    return inner


import time
def fun_run_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        s_time = time.time()
        ret = func(*args, **kwargs)
        e_time = time.time()
        print("{} cost {} s".format(func.__name__, e_time-s_time))
        return ret
    return inner


@fun_run_time
def test():
    for i in range(5):
        time.sleep(2)


# word = 'hi Ther'
# print(lowerWord(word))

test()