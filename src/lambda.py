#Higher order functions(HOF) : Takes functions as arguments and returns functions
#Lanbda functions:anonymous functions usually arguments/return to HOF

def myfunc(n):
    return lambda a: a * n


my_doubler = myfunc(2)
my_tripled = myfunc(3)

print(my_doubler(11))
print(my_tripled(11))

