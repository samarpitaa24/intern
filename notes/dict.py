# 2 methods to add items (entire key value pair) => thisdict["color"] = "red" and using upate({:})

#ordered ahe

#update({:}) if key is existing then updates value else creates new pair

#access using index or using key or get(key)

d1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#reurns pair
for i in d1.items():
    print(i)
    
for x,y in d1.items():
    print(x,y)
    print("keys",d1[x])
    
student = {
           "stud1" : {"roll_no" : "01" , "name" : "abc"},
           "stud2" : {"roll_no" : "02" , "name" : "abc"},
           "stud3" : {"roll_no" : "03" , "name" : "abc"}
           }

d1.keys()
d1.values()


d1.popitem() #Removes the last inserted key-value pair
d1.pop()

d1.fromkeys()	#Returns a dictionary with the specified keys and value
'''
Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)'''

a= d1.copy()