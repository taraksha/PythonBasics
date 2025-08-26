#LIST uses [] ordered, mutable, allows duplicates, any datatype
from typing import List
# always use copy() to copy the contents of the datatype = will only copy the reference hence it will change as the source changes
mylist = ["apple", 1 , "cherry"]
mylist2 = list(["using","constructor"])

print(mylist)
print(type(mylist))#<class 'list'>

print(len(mylist)) #3
print(mylist[-1]) #cherry
if "apple" in mylist:
    print("Yes, we have apple")

#['apple', 1, 'cherry']
mylist[1] = "banana" #update the list at the given position
#['apple', 'banana', 'cherry']
mylist[1:3] = ["blackcurrant", "watermelon"]  #update the list at the given positions
print(mylist)
mylist[1:2] = ["coconut", "chocolate"]  #update the given position alone
print(mylist)
mylist[1:5] = ["new"]   #update the given position alone
print(mylist)
mylist[1:1] = ["Actual insert"]  #insert at the provided position
print(mylist)
mylist.insert(2,"afterInsertAt2")
print(mylist)
mylist.append("afterAppend")
print(mylist)

tropical = ["ExtendMango", "pineapple", "papaya"]
mylist.extend(tropical) #can extend other datatypes too
print(mylist)

#Remove
mylist.remove("Actual insert")
print(mylist)
mylist.pop() #removes last element
print(mylist)
mylist.pop(1) #removes element at the given position
print(mylist)
del mylist[1] #deletes at the index
print(mylist)
del mylist #deletes the list. cant be accessed after that. Throws error
mylist2.clear() #clears the contents
print(mylist2)


#Loop
list = []
for i in range(5):
    list.append(i) #create new list
print(list)

for i in list:
    print(i)

[print(x) for x in list]

#Comprehention
fruits = ["apple", "banana", "cherry", "kiwi", "mango","KIWI"]
#newlist = [expression for item in iterable if condition == True]
newfruits = [x.upper() for x in fruits if "a" in x]

print(newfruits)

editedfruits = [x if x != "banana" else "orange" for x in fruits]
print(editedfruits)
print("")

#Sort
sortlist = ["apple", "banana", "cherry", "kiwi", "mango","KIWI"]
sortlist.sort() #sorts from Uppercase to lowercase
print(sortlist)
sortlist.sort(key = str.lower)
print(sortlist)
sortlist.sort(reverse=True)
print(sortlist)
sortlist.reverse()
print(sortlist)

print(sortlist.count("kiwi"))# counts the no of occurances

#join
joinedlist = fruits+sortlist
print(joinedlist)
joinedlist.clear()
joinedlist=fruits.copy()
print(joinedlist)


joinedlist = sortlist[:]
print(joinedlist)