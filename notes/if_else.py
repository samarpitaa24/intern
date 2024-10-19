#A - 1-10
#B - 11-20
#C - 21-30

roll = 23

if roll in range (1,11):
    print("A")
elif roll in range(11,21):
    print("B")
elif roll in range(21,31):
    print("C")   
else : 
    print("doesn't belong anywhere")
    
roll1 ='' #empty ahe so false , works same for [] , {}
if not roll1 :  #here var acts as 1 or 0 ie tya var madhe kahitri ahe
    print(" not exists") 
    
    
roll2= {"k":"v"}
if roll2 :  #here var acts as 1 or 0 ie tya var madhe kahitri ahe
    print(" exists") 

    
a= False
if a : #here it considers a as 0 bcoz false
    print("if")
else :
    print("else")
    
#try for checking existence of value or key in list and dict