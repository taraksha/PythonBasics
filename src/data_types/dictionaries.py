#Dictionary is a collection which is ordered** and changeable. No duplicate members.{ :, }

#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#The items() method will return each item in a dictionary, as tuples in a list.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(type(thisdict)) #<class 'dict'>
print(thisdict.get("model")) # "Mustang"
keys = thisdict.keys()
print(keys) # dict_keys(['brand', 'model', 'year'])

thisdict["color"] = "white" #Update
print(keys) #dict_keys(['brand', 'model', 'year', 'color'])

print(thisdict.values()) #dict_values(['Ford', 'Mustang', 1964, 'white'])


print(thisdict.items()) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'white')])

thisdict.update({"year": 2020}) # can be new or existing
print(thisdict)

thisdict.pop("model")
print(thisdict) #{'brand': 'Ford', 'year': 2020, 'color': 'white'}

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

del thisdict["year"] # throws error if the key is not present


for x in thisdict:
    print(x,":",thisdict[x])

for x, y in thisdict.items():
    print(x, y)

mydict = dict(thisdict)
print(mydict)

#Nested Dictionary
myfamily = {
    "child1" : {
        "name" : "Tanisha",
        "year" : 2016
    },
    "child2" : {
        "name" : "Raksha",
        "year" : 2019
    }
}
print(myfamily)

""" or else

 child1 = {
        "name" : "Tanisha",
        "year" : 2016
    }
    child2 = {
        "name" : "Raksha",
        "year" : 2019
    }
myfamily = {
  "child1" : child1,
  "child2" : child2
}

"""

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print("\t"+y + ':', obj[y])