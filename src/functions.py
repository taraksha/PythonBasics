"""
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
"""

call_count = 0
print("This line will be printed if functions.py  module is imported by others")

def my_function(fname, lname):
    print(fname + " " + lname)


# to receive many arguments, arguement come in as a tuple
def my_kids(*kids):
    print("The youngest child is " + kids[2])


# use key=value syntax to send in any order
def unordered_args(child3, child2, child1):
    print("The youngest child is " + child3)


# use keyword args ** to get arguments as a dictionary
def kw_args(**kid):
    print("Your last name is " + kid["lname"])
    print(kid.keys())


# Function can have default parameter value
def my_country(country="India"):
    print("I am from " + country)


'''
# ",/" after the argument allows positional arguments alone, keyword arguments will throw error(3.6 doesnt support)
def positional_args(x, /):
    print(x)
positional_args(x = 3)

"*," before the argument allows keyword arguments alone, positional arguments will throw error
def positional_args(*,x):
    print(x)
positional_args(x = 3)
'''

"""
#You can combine the two argument types in the same function.
#Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

def combined_args(a, b, /, *, c, d):
    print(a + b + c + d)
combined_args(5, 6, c = 7, d = 8)
"""


# Recursion
# Quick Sort
def quick_sort(unordered_list):
    quick_sort_with_bounds(unordered_list,0,len(unordered_list)-1)


def quick_sort_with_bounds(unordered_list, left_pointer, right_pointer):
    global call_count
    call_count += 1

    if left_pointer < right_pointer:
        seperator_pointer = partition(unordered_list,  unordered_list[right_pointer], left_pointer, right_pointer)
        swap(unordered_list, right_pointer, seperator_pointer)
        quick_sort_with_bounds(unordered_list, left_pointer, seperator_pointer - 1)
        quick_sort_with_bounds(unordered_list, seperator_pointer + 1, right_pointer)


def partition(unordered_list, pivot, left_pointer, right_pointer):
    while left_pointer < right_pointer:
        while pivot >= unordered_list[left_pointer] and left_pointer < right_pointer:
            left_pointer += 1
        while pivot <= unordered_list[right_pointer] and left_pointer < right_pointer:
            right_pointer -= 1
        swap(unordered_list, left_pointer, right_pointer)
    return left_pointer


def swap(unordered_list, pointer1, pointer2):
    unordered_list[pointer1], unordered_list[pointer2] = unordered_list[pointer2], unordered_list[pointer1]

#Below part executes only when the module is run directly
if __name__ == "__main__":

    number_list = [504,40,304,23,250,10,39]
    print("Quick sort:", number_list)
    quick_sort(number_list)
    print("function call count:", call_count)
    print(number_list)

    my_country("Sweden")
    my_country()

    my_function("Asha", "Selvaraj")

    my_kids("Anitha", "Asha", "Aravinth")

    unordered_args(child1="Emil", child2="Tobias", child3="Linus")

    kw_args(fname="Asha", lname="Selvaraj")

