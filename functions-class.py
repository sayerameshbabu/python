#!/usr/local/bin/python3
# def function1(**var2):
#     return type(var2)
# print(function1(a="hello",b="adff"))

# def sum(a,b,symbol="+"):    
#     if symbol == "+":
#        return a+b
#     return "nota a valid symbol"

# print(sum(2,symbol="+",b=2))

# def add_numbers(*numbers):
#     def inner_add(number):
#         if number == []:
#             return 0
#         if number != []:
#             return number.pop()+inner_add(number)
#     return inner_add(list(numbers))

# print(add_numbers(12,23,23))
    

# def sum_num(**kwargs):
#     print(kwargs)
# sum_num(a="dfa",b=1)

def outer_function(number):
    def inner_funtion(value):
        return number*value
    return inner_funtion

print(outer_function(12)(value=12))