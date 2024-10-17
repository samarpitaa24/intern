'''Problem 3: ATM Simulator

Create an ATM simulator that allows users to perform basic banking operations. The program should:
Store the user's balance in a variable.
Provide options to check the balance, deposit money, and withdraw money.
For withdrawals, use if-else statements to ensure the withdrawal amount doesn't exceed the balance.
Use a while loop to allow the user to perform multiple operations until they choose to exit'''

users = {
    "u1" : {"id" : 1 , "balance" : 5000 },
     "u2" : {"id" : 2 , "balance" : 3000 },
     "u3" : {"id" : 3 , "balance" : 6000 }
}

flag =1

ID_ = int(input("enter id : "))
print("operations : 1. Show balance \n2. Deposit \n3. Wthdrawl")


while flag :
   
    op = int(input("enter operation no. : "))
    
    
    if op == 1 :
        #show bal
        for x,y in users.items():
            b_id = y.get("id")
            if ID_ == b_id :
                print(y.get("balance"))
    
    elif op == 2 : 
        #for deposit             
        for x,y in users.items():
            d_id = y.get("id")
            if ID_ == d_id :
                bal2 = y.get("balance")
                dep = int(input("enter amt to be deposited : "))
                new_bal2 = bal2 + dep 
                # users.update({x:{"balance" : new_bal2}})
                users[x] = {"balance" : new_bal2}
        print(users)
    
    elif  op ==3 :
        #for withdrawl
        for x,y in users.items() :
            ident = y.get("id")
            if ID_ == ident :
                w_amt = int(input("enter withdrawl amt : "))
                bal = y.get("balance")
                if w_amt <=bal :
                    new_bal = bal-w_amt
                    users.update({x : {"balance" : new_bal }})
                else :
                    print("balance insufficient")          
        print(users)

    cont = input("do you wanna continue : ")
    if cont == 'y' or cont == 'Y' :
        flag = 1
    else :
        flag = 0    
    
    

# #for withdrawl
# ID_ = int(input("enter id : "))
# for x,y in users.items() :
#     ident = y.get("id")
#     if ID_ == ident :
#         w_amt = int(input("enter withdrawl amt : "))
#         bal = y.get("balance")
#         if w_amt <=bal :
#             new_bal = bal-w_amt
#             users.update({x : {"balance" : new_bal }})
#         else :
#             print("balance insufficient")          
# print(users)


# #for deposit             
# for x,y in users.items():
#     d_id = y.get("id")
#     if ID_ == d_id :
#         bal2 = y.get("balance")
#         dep = int(input("enter amt to be deposited : "))
#         new_bal2 = bal2 + dep 
#         users.update({x:{"balance" : new_bal2}})
# print(users)
            
# #show bal
# for x,y in users.items():
#     b_id = y.get("id")
#     if ID_ ==b_id :
#         print(y.values("balance"))