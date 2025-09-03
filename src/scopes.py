#scopes Local->Enclosing(nested function)->Global->BuiltIn

#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

#The global keyword makes the variable global.

#Also, use the global keyword if you want to make a change to a global variable inside a function.

x,y,z = 300,500,700


def myfunc():
    global x
    x = 1
    y = 2
    print("inside myfunc():",x,y,z)


myfunc()
print("outside myfunc():",x,y,z)
