#LIST uses [] ordered, mutable, allows duplicates, any datatype
mylist = ["apple", 1 , "cherry"]
print(type(mylist))
print(len(mylist))
print(mylist[-1])
if "apple" in mylist:
    print("Yes, we have apple")
mylist[1] = "banana" #update the list at the given position
print(mylist)
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



#TUPLE is a collection which is ordered and unchangeable. Allows duplicate members.

#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

#Dictionary is a collection which is ordered** and changeable. No duplicate members.