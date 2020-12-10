import random


def jumble(funcobj):  # decorator function

    def wrapper(inputstr):  # wrapper function
        L = list(inputstr)
        random.shuffle(L)
        inputword = ''.join(L)
        return funcobj(inputword)

    return wrapper



def modifystring(s):
    return ' '.join([c.upper() for c in s])

# ---------------------------------------

print(modifystring('pineapple'))


modifystring = jumble(modifystring)
print('--->', modifystring)


print(modifystring('pineapple'))  # plaeps


'''

A P P L E S

P L A E P S  <= jumbled up form of the string

'''
