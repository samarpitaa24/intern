#for withdrawl
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