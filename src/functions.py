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