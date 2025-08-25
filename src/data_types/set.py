# Set is a collection which is unordered, unchangeable*, and un indexed. No duplicate members.{}

#Set items are unchangeable(Can't update), but you can remove items and add new items.

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

#Note: If the item to remove does not exist, remove() will raise an error.But discard() doesnt

thisset = {"apple", "banana", "cherry","cherry",1,2,3,False,True}
print(thisset) #{False, 1, 2, 3, 'apple', 'banana', 'cherry'}
print(type(thisset)) #<class 'set'>
print("banana" in thisset) #True

"""METHODS 
    add(item),
    update(set) - adds from another collection,
    remove(item) - error if not present,
    discard(item) - remove, no error if not present
    pop() - removes randomly
    clear()
    del setname
Joins
     union()  - all , can be used with other collections too
     update()(|=) - all, it updates the original set, and does not return a new set,can be used with other collections too
     |        - all, only set
     intersection()        - only duplicates, any data type, returns new set
     intersection_update()(&=) - only duplicates, any data type, updates the set
     &                     - only duplicates, only sets
     difference()        - returns the items that are only in the first set
     -                   - same as difference(), only uses set
     difference_update()(-=) - same as above,it updates the original set
     symmetric_difference(),symmetric_difference_update()(^=),^ - keeps all items EXCEPT the duplicates,same as above
     
     isdisjoint()	 	Returns whether two sets have a intersection or not
     issubset()   <=	Returns True if all items of this set is present in another set
            	    <	Returns True if all items of this set is present in another, larger set
     issuperset()	>=	Returns True if all items of another set is present in this set
                	>	Returns True if all items of another, smaller set is present in this set

"""
thisset.add("strawberry")
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset.remove("cherry")
thisset.discard(1)
print(thisset)

#JOINS
set1 = {1,2,3}
set2 = {4,5,6}
set3 = set1 | set2 | tropical
print(set3) #{1, 2, 3, 4, 5, 6}
print(set1 & set3)
print(set3 - set1)
print(set2 ^ set3)
print(set2 ^ set1)
print(set3)
set3-=set2
print(set3)
print(set2.isdisjoint(set3))
print(set1>set3)