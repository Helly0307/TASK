#The pop() method removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)



#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)



#add items in dict
thisdict["brand"]="ford"
thisdict["model"]="Mustang"
thisdict["year"]=2020
print(thisdict)



#The del keyword removes the item with the specified key name
del thisdict["model"]
print(thisdict)



#the clear() method empties the dictionary
thisdict.clear()
print(thisdict)



#The del keyword can also delete the dictionary completely
del thisdict
print(thisdict)       #this will cause an error because "thisdict" no longer exists.




