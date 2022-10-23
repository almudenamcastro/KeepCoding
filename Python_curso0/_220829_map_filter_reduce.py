''' 
list comprehension:
applies a function to a list, and can also filter it. 
mind the brackets

[funcion(x) for x in list]
'''

["*"+x+"*" for x in ["hola", "casa", "tú"]]
["*"+x+"*" for x in ["hola", "casa", "cacatúa", "tú"] if x[0]=="c"]


'''
map:
applies a function to a list. 
map(function, list, ...)
to see the result -> you need to turn it into a list or duple
'''

map(lambda x: "*"+x+"*", ["casa", "hola", "tú"])
list(map(lambda x: "*"+x+"*", ["casa", "hola", "tú"]))

'''
filter
filters a list based on a boolen function (condition for true)

filter(bool function, list, ...)
'''

list(filter(lambda x: x[0].lower()=="p", ["papa", "pero", "aguacate"]))

list(filter(lambda x: len(x) > 2 and x[2].lower()=="p", ["papa", "pero", "aguacate", ""]))

'''
reduce
returns an iterable sum. s -> suma, n -> next
reduce(function (s, n), list)
3rd param: you can include an initilizer
'''
from functools import reduce
from _220829_sumatodos import sumatorio


reduce (lambda s, n: s + n*n, [0,1,2,3])
reduce (lambda s, n: s + n*n, [0,1,2,3], 0)

sumatorio(15, lambda x:2*x +1)
reduce(lambda s, n: s + 2*n +1, list(range(15+1)), 0)

'''recursion
iteración funcional. 
ojo, en python no es eficiente, existe un máximo de recursión
import sys
print(sys.getrecursionlimit())
'''

def sumatoriorec(n):
    if n==1:
        return 1
    else: 
        return n + sumatoriorec(n-1)