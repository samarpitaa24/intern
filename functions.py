#default arg is given cause jarka args expected 2 ahet, pan user ne 1 pass kelay so error yeil , toh yeu naye mhnun

#runtime errors are those je code lihilyavar disat nahi pan run kelyavar yetat , tyanna we handle using try catch block

#positional args are those for who order of input matters
#keyword args


#positional & default args 
def my_function(fname, lname = ""): #empty string pan okay
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

#arbitrary args => any no of args
roll =[]
def mark_attendance(*r ):
    for i in r :
        roll.append(i) #roll is global , accessible throught the prog
    print(roll)
mark_attendance(1,2,3,4,5)

#keyword args 
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Arbitrary Keyword Arguments, **kwargs => If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"]) #kid["lname"] is of dict datatype
my_function(fname = "Tobias", lname = "Refsnes")


#return => acts as break for func, it must be written as last statement only 
def cal(x):
  return 5 * x , x - 5 ,x + 5  #returns multiple values in tuple format
mult , sub , add = cal(10) #tuple values directly assigned
print(mult , sub , add)

