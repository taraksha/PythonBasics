
print(__file__)#python built in variable, used to print the filename

a = 10
b = 'Asha'
c = "Name"
d = "234"
e = 10.2
f = True #bool
"""
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "",
 the number 0, and the value None. And of course the value False evaluates to False.

ojects are False if its __len__ is zero
"""

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(int(d)))
print(type(e))
print(type(f))

x, y, z = "Orange", "Banana", "Cherry"
print(x,y,z)

"""
import random

print(random.randrange(1, 10))

"""


"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""