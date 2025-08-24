#TUPLE is a collection which is ordered and unchangeable. Allows duplicate members.()

thistuple = ("apple", "banana", "cherry")
print(thistuple)


#NOT a tuple , its a string
thistuple = ("apple")
print(type(thistuple))

#Single Tuple
thistuple = ("apple",)
print(type(thistuple))

#access : same as list.
#Modification work around. Tuple->list(modify)->Tuple

addTuple = ("banana",)
thistuple += addTuple
print(thistuple)

#UNPACKING
(red,yellow) = thistuple
print(f"red is :{red},yellow is: {yellow}")

unpack =(1,2,3,4,5,6,7,8,9,10)
(num1,num2,*rest ) = unpack #unpacks the * variable with the rest of tuple into a list
print(rest)
print(type(rest))

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
