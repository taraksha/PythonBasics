"""
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
"""

def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Asha", "Selvaraj")


#to receive many arguments, arguement come in as a tuple
def my_kids(*kids):
    print("The youngest child is " + kids[2])
my_kids("Anitha", "Asha", "Aravinth")


#use key=value syntax to send in any order
def unordered_args(child3, child2, child1):
    print("The youngest child is " + child3)
unordered_args(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#use keyword args ** to get arguments as a dictionary
def kw_args(**kid):
    print("His last name is " + kid["lname"])
    print(kid.keys())
kw_args(fname = "Asha", lname = "Selvaraj")


#Function can have default parameter value
def my_country(country = "India"):
    print("I am from " + country)
my_country("Sweden")
my_country()

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

#Recursion
#Quick Sort

def quick_sort(list,left_pointer,right_pointer ):
    if left_pointer >= right_pointer:
        return
    pivot = list[right_pointer]
    seperator_pointer = partition(list,pivot,left_pointer,right_pointer)
    swap(list,right_pointer,seperator_pointer)
    quick_sort(list,left_pointer,seperator_pointer-1)
    quick_sort(list,seperator_pointer+1,right_pointer)

def partition(list,pivot,left_pointer,right_pointer):
    while(left_pointer < right_pointer):
        while(pivot >= list[left_pointer] and left_pointer < right_pointer):
            left_pointer += 1
        while(pivot <= list[right_pointer] and left_pointer < right_pointer):
            right_pointer -= 1
        swap(list,left_pointer,right_pointer)
    return left_pointer

def swap(list,  first, second):
    temp = list[first]
    list[first] = list[second]
    list[second] = temp

list = [2,3,1,343,56,5,4]
print("Quick sort:",list)
quick_sort(list,0,len(list)-1)
print(list)
