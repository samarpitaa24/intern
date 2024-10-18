#break exits both if cond and for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break #terminates if cond and also if cond

#continue exits if cond only
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": #skips only this cond
    continue
  print(x)
  
#pass fakta error yeu naye mhnun asta,otherwise doesnt do anything
for x in [0, 1, 2]:
	print(x)
pass
	
for x in [0, 1, 2]:
  pass

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    pass  #everything w get printed
  print(x) 
  # print(fruits)