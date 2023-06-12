#!/usr/local/bin/python3
# def factorial(number):
#     result=1
#     for x in range(1,number+1):
#         if x>1:
#             result=result*x
#     return result

# print(factorial(3))

def factorial_outer(number):
    if number < 0 :
        raise ValueError("Sorry. 'number' must be zero or positive.")
    def factorial_inner(number):
        if number<=1:
            return number
        else:
            return number*factorial_inner(number-1)
    return factorial_inner(number)

print(factorial_outer(-4))