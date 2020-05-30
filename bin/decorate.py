def lowerWord(word='Hi There'):
    return word.lower()

from functools import wraps
def start_word_upper(func):
    @wraps(func)
    def inner(*args,**kwargs):
        word = func(*args,**kwargs)
        return word.captialize()
    return inner


word = 'hi Ther'
print(lowerWord(word))
