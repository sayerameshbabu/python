#!/usr/local/bin/python3
def outer_function(number):
    def inner_function():
        print("this statement is from inner function:- ",number)
    x=inner_function
    return x

def function(var):
    print("this is a plain function, ",var)

y=function
print(y(2))


