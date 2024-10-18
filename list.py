#mutable

#list methods

"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value

extend()	Add the elements of a list (or any iterable), to the end of the current list 
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars) 

index()	Returns the index of the first element with the specified value 

insert()	Adds an element at the specified position
fruits.insert(1, "orange")

pop(pos)	Removes the element at the specified position
remove( element )	Removes the first item with the specified value

reverse()	Reverses the order of the list    
sort()	Sorts the list cars.sort(reverse=True) => sorts in desc
"""

#capitalizing b of banana
fruits = ["apple ", "banana", "cherry"]

#1 sol
for i in range (len(fruits)):
  print(fruits[i])
  if fruits[i] == "banana" :
    fruits[i] = "Banana"
print(fruits)

#2 sol    
a =0 
for i in fruits:
  print(i)
  if i == "banana" :
    fruits[a] = i.capitalize()  #or use index() to get the index of that i and store it in a var, then use that index to replace item
    a+=1 #to find index
print(fruits)
    