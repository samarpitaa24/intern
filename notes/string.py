#immutable

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
swapcase()
capitalize() => first letter capital rest all are converted into lowercase
casefold() => all lowercase

center(no.) => centers string in space no. mentioned
find("word") => returns pos of first char where it is found and counts from 0 
index("word") => same as find

splitlines() => splits string wherever newline \n is found and is converted into list of srings
.splitlines(True) => even mentions \n in the list of string  ['Thank you for the music\n', 'Welcome to the jungle']

x = "#".join(myTuple)
x = txt.ljust(20) =>adds spaces and makes it left justified

lstrip()
strip()  => trims the blank spaces
rstrip()

startswith()
endswith()  => returns bool

expandtabs() => increase tabs size

count()
"""


#built in
""" 
Check if all items in a list are True:
mylist = [True, True, True]
x = all(mylist)

any()	Returns True if any item in an iterable object is true
mylist = [False, True, False]
x = any(mylist)


The ascii() function will replace any non-ascii characters with escape characters:
x = ascii("My name is Ståle") =>'My name is St\e5le'

chr(97)
ord()	Convert an integer representing the Unicode of the specified character

enumerate()  =>Convert a tuple into an enumerate object 
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]

dict()
pow()

filter()	Use a filter function to exclude items in an iterable object     


"""

a = "Hello I Am Samarpita"
print(a.capitalize())

txt = f"My name is John, I am {5+2}"
print(txt)

#use it w input, input directly name , surname, city , etc 