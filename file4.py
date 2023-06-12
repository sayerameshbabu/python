#!/usr/local/bin/python3

def outer_function(number):
    def inner_funcion():
        print("this is inner function, with ", number)
        return "hi"
    return inner_funcion

outer_function(12)()


number = 4
result=1
for x in range(1,number+1):
    result=x*result

# print("the factorial is", result)



def outer_fac(number):
    def inner_factorial(number):
        if number > 1 :
          return number * inner_factorial(number-1)
        else:
          return 1
    return inner_factorial(number)

# print(outer_fac(5))

def outer_multiplier(number):
   def inner_multiplier(value):
      return number * value
   return inner_multiplier

# print(outer_multiplier(5)(9))

def higher_order_function(func):
   def inner_order_function():
      print("this is before function")
      func()
      print("this is after function-----")
   return inner_order_function

@higher_order_function
def func1():
   print("this is during function 1")

@higher_order_function
def func2():
    print("this is during function 2")



func2()
func1()
