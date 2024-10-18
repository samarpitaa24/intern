library = { "book1 " : {"title" : "Limitless" , "author" : "Jim Kwik" ,"year" : 1960, "status" :"avail"},
           "book2 " : {"title" : "Death on the Nile" , "author" : "Agatha Christie" ,"year" : 1970,"status" :"avail"},
           "book3 " : {"title" : "Murder on the orient express" , "author" : "Agatha Christie" ,"year" : 1980, "status" :"avail"}
           }

#add book
def add_book():
        book_count = 3
        new_book = f"book{book_count+1}"
        Title = input("Enter Title : ")
        auth = input("Enter author : ")
        year = int(input("Enter year : "))
        stat = input("Enter stat: ")
        library[new_book]={"title" :Title , "author" : auth, "year" : year ,"status": stat }
        book_count +=1
        print(library[new_book].items())
               
#borrow or return book
def borrow():
    which_book = input("enter the book name : ")
    for x,y in library.items() :
       title =  y.get("title")
       if which_book == title :
           library[x].update({"status": "not avail"})
           print(library[x].items())
           
def return_book():
    which_book = input("enter the book name : ")
    for x,y in library.items() :
       title =  y.get("title")
       if which_book == title :
           library[x].update({"status": "avail"})
           print(library[x].items())
           
# display books using for loop
def display() :
    for x,y in library.items() :
        print(library[x].items())
        
#search books
def search_book():
    for x,y in library.items():
        search_book = input("enter book name or author name : ")
        book_name = y.get("title")
        auth_name = y.get("author")
        if (search_book == book_name) or (search_book == auth_name) :
            print(library[x].values())
            
search_book()