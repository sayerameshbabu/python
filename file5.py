#!/usr/local/bin/python3

# 1. Write a Python function to find the maximum of three numbers. 
def max_function(*values):
    temp=values[0]
    for x in list(values):
        if x>temp:
            temp=x
    print(f"max number is {temp}")
    return temp

# 2. Write a Python function to sum all the numbers in a list. 
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 

def sum_all_numbers(*numbers):
    sum=0
    for x in numbers:
        sum=sum+x
    return sum


# 3. Write a Python function to multiply all the numbers in a list. 
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336 

def multiply_numbers(*numbers):
    


# 12. Write a Python function that checks whether a passed string is a palindrome or not. 
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

# 18. Write a Python program to execute a string containing Python code. 
