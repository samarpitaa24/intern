''' anonymous function.
 can take any number of arguments, but can only have one expression.'''
 
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n


#import datetime
#for arrays, use Numpy lib during dsa

