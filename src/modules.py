from functions import quick_sort
import oops.inheritance as inheritance #import from other package
import platform #built in module

print(platform.system())
print(platform.python_version())

unordered_list = [2,32,56,3,5,234,63,2]
print("Before Ordering:",unordered_list)
quick_sort(unordered_list)
print("After Ordering",unordered_list)


print(dir(inheritance)) #lists all the function names (or variable names) in a module
car = inheritance.Car("Ford", "Mustang")
print(car.brand)
car.move()
