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
  
  for x in range(1, 30, 2): #default step is 1 , 2 for even(start 0) and odd start(1) 
   print(x)
   
 #for sobat else use hoto  
for x in range(6):
  print(x)
else:  #he for execute zhala tarch execute honar, jar for madhe break zhala tr mag else part execute honar nahi 
  print("Finally finished!")
  
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": 
    for y in x : #x madhe already banana ahe currently
      print(y)