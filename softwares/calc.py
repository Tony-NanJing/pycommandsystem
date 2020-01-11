#!python3
#-*-coding:UTF-8-*-
#pycs calculator
from math import *

while True:
    try:
        inp = input()
        if inp == 'q':break
        ans = eval(inp)
        print(ans)

    except NameError:
        print('Error')

    except ZeroDivisionError:
        print('ZeroDivisionError')

    except SyntaxError:
        print('Error')
        
