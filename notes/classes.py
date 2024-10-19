'''class is a structure , object is a copy of that structure and the functions we can use on the obj'''

#self is a keyword reprrsenting the object 
#The __init__() function is called automatically every time the class is being used to create a new object.

class Number :
    def __init__(self,num):
        self.num = num  #self represents obj var
        
    # def rev(self) :
    #     convert = str(self.num) #all these variables are of method
    #     reversed = convert[::-1]
    #     numb = int(reversed)
    #     return numb
    #add exception of 0 at start and end  , like 1000 should bcome 1 like remove 0's
    #self.reversed becomes object cha variable which is accessible using object name
    
    def rev(self) :
        inp_to_str =str(self.num)
        rev_str = inp_to_str[::-1]
        return int(rev_str)

num1 = Number(34567)
rev_num = num1.rev()
print(num1.num ,',',rev_num)

#fan speed decrease after 30 mins : save starting time , check curr_time == starting_time +30 , then decrease speed

#webscraper using gmap ,fetch area wise business data

