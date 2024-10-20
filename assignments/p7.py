'''create a module and import it in another file and use the function from the module'''

import module

number = int(input("enter numbers to be reversed : "))
rev_num = module.rev(number)
print(f"for {number} reversed number is ",rev_num )