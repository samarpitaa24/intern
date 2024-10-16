#string acts as an array hence slicing can be done
print("hello" [2])

#act as collection hence looping can be done
for i in "rhythm" :
    if i in "aeiou" :
        print("vowel")
    else :
        print("consonant")
        
#can check for word or character in string (in / not in)
sent = "i am a student"
print("yes" if "student" in sent else "no")

""" 
.upper()
.lower()
.strip() -> removes whitespaces at the beginning and end of the string only

.replace() -> can replace a character from the string or even a word
a = "Hello, World!"
print(a.replace("H", "J"))

.split(,) -> , stands for separator which can be defined while spliting of the string

"""

#strings concatenated

#formatting of strings (adding var containing no. to a string)
""" 
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"  //op -> 59.00 (containing 2 decimals)
print(txt)

{20 * 50} math op is also possible (*, + ,- , /)
"""

#escape character
txt = "We are the so-called \"Vikings\" from the north."
# "" issue wont occur
txt2 = 'It\'s alright.'
txt3 = "This will insert one \\ (backslash)." #=> This will insert one \ (backslash).

# \n \t \b(removes backspaces)

"""
capitalize() => first letter capital
casefold() => all lowercase
center(no.) => centers string in space no. mentioned

"""