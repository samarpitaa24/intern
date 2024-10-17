# 2 methods to add items (entire key value pair) => thisdict["color"] = "red" and using upate({:})
#ordered ahe

d1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for i in d1.items():
    print(i)
    
for x,y in d1.items():
    print(x,y)
    print("keys",d1[x])