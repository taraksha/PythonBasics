#IF and ELSE
a = 200
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#short hand
if a > b: print("a is greater than b")
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")

if b > a:
    pass
#to avoid error

#MAtch - like switch (available from 3.10)
"""
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
"""

#LOOPS
#while
i = 1
while i < 6:
    print(i)
    if i == 3:
        break #continue - to skip to the begining
    i += 1

i = 6
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")  #i think this else is unnecessary, wont be executed if there is a break

#For : can even iterate through strings,range
for x in range(2, 30, 3):
    print(x) #Note range is  2 to 29(in general 0 to n-1)