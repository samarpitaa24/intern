import mysql.connector
from  datetime import *



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shirish@24",
  database="library"
)

mycursor = mydb.cursor()

def add_books() :
  
    b_id = int(input("Enter book id : "))
    b_name = input("Enter book name : ")
    b_auth = input("Enter book author : ")
    status = input("Enter book status : ") 
    b_year = int(input("Enter year : "))
    n_of_bks = int(input("Enter no of books : "))
    
    q1 = "INSERT INTO books (id, book_name, author, year,status, no_of_books ) VALUES (%s, %s, %s, %s,%s,%s)"
    t1 = (b_id, b_name, b_auth,b_year, status,n_of_bks) 
    mycursor.execute(q1,t1)
    mydb.commit()
    print(f"{b_name} written by {b_auth} is saved in records.")
# add_books()

def display_books():
  mycursor.execute("SELECT * FROM books")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
# display_books()


#search books
def search_book():
    search_book = input("enter book name : ")
    
    mycursor = mydb.cursor()
    q1 = "SELECT * FROM books WHERE book_name = %s "
    book = (search_book,)
    mycursor.execute(q1,book)
    myresult = mycursor.fetchall()
    return myresult
    

#update  books
def update_book_details():
    curr_book = input("enter book name : ")
    update_what = input("Update what ? : ")
    
    if update_what == "name":
      new_name = input("enter book name : ")
      mycursor = mydb.cursor()
      q1 = "UPDATE books SET book_name = %s WHERE book_name = %s"
      
      book = (new_name, curr_book)
      mycursor.execute(q1,book)
      
      q2 = "SELECT * FROM books WHERE book_name = %s"
      book = (new_name,)
      mycursor.execute(q2,book)
      myresult = mycursor.fetchall()
      print(myresult)
      
    elif update_what == "author":
      new_auth = input("enter author name : ")
      mycursor = mydb.cursor()
      q1 = "UPDATE books SET author = %s WHERE book_name = %s"
      
      book = (new_auth, curr_book)
      mycursor.execute(q1,book)
      
      q2 = "SELECT * FROM books WHERE book_name = %s"
      book = (curr_book,)
      mycursor.execute(q2,book)
      myresult = mycursor.fetchall()
      print(myresult)
      
    elif update_what == "no. of books":
        new_count = int(input("enter new book count : "))
        mycursor = mydb.cursor()
        q1 = "UPDATE books SET no_of_books = %s WHERE book_name = %s"
        
        book = (new_count, curr_book)
        mycursor.execute(q1,book)
        
        q2 = "SELECT * FROM books WHERE book_name = %s"
        book = (curr_book,)
        mycursor.execute(q2,book)
        myresult = mycursor.fetchall()
        print(myresult)
        
    elif update_what == "year":
        new_year = int(input("enter year : "))
        mycursor = mydb.cursor()
        q1 = "UPDATE books SET year = %s WHERE book_name = %s"
        
        book = (new_year, curr_book)
        mycursor.execute(q1,book)
        
        q2 = "SELECT * FROM books WHERE book_name = %s"
        book = (curr_book,)
        mycursor.execute(q2,book)
        myresult = mycursor.fetchall()
        print(myresult)
        
    elif update_what == "status":
        new_status = int(input("enter status : "))
        mycursor = mydb.cursor()
        q1 = "UPDATE books SET status = %s WHERE book_name = %s"
        
        book = (new_status, curr_book)
        mycursor.execute(q1,book)
        
        q2 = "SELECT * FROM books WHERE book_name = %s"
        book = (curr_book,)
        mycursor.execute(q2,book)
        myresult = mycursor.fetchall()
        print(myresult)   
# update_book_details()
    

# add student details and the book issued and date of issue 
# compare to the issued date + 7 and then if within , no penalty , if after then penalty

# date in yyyy/mm/dd format

def update_no_of_books_issue(bookid):
    mycursor = mydb.cursor()
    # selcts current number of books
    q1 = "SELECT no_of_books FROM books WHERE id = %s"
    bkid = (bookid,)
    mycursor.execute(q1, bkid)
    nofbk = mycursor.fetchone()  # fetch only one record
    
    nofbk = nofbk[0]  # nofbk is a tuple, so extract the first element
    if nofbk is None: # where no_of_books is NULL
        print(f"Number of books for ID {bookid} is not set.")
        return
    if nofbk > 0: # if bk avail then decrease by 1
        nofbk -= 1
    else:
        print("No more books available to issue.")
        return

    # update no of books 
    q2 = "UPDATE books SET no_of_books = %s WHERE id = %s"
    updated = (nofbk, bookid)
    mycursor.execute(q2, updated)
    mydb.commit()
    
    print('Number of books updated')

def display_student():
  mycursor.execute("SELECT * FROM student")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def issue_book():
  studid = int(input ("Enter student id : "))
  studname = input("Enter student name : ")
  i_book = search_book() #list of tuple
  pen =0
  print(i_book)
  for i in i_book : #for tuple in list
    for j in i : # for item in tuple
      if j == "available" :  #if item = available
        q1 = "INSERT INTO student (stud_id,name,book_id,book_name , date_of_issue,penalty) VALUES (%s,%s,%s,%s,%s,%s)"
        bookid = i[0]  #tuple[0]
        bookname = i[1]
        d1 = date.today()
        details = (studid,studname , bookid,bookname,d1 , pen)
        mycursor.execute(q1,details)
        mydb.commit()
        update_no_of_books_issue(bookid)
        print("student added ")
        display_student()

# issue_book()
         
def penalty (studid):
 
  mycursor = mydb.cursor()
    # selcts date of issue and return
  q1 = "SELECT date_of_issue, date_of_return FROM student WHERE stud_id = %s"
  stid = (studid,)
  mycursor.execute(q1, stid)
  dates = mycursor.fetchone()  # fetch only one record
  
  d1, d2 = dates
  expected = d1 + timedelta(7) 
  
  if d1 < d2 <= expected : #comparing return date w issue date and expected return date
    return 
  elif expected < d2 <= (expected+ timedelta(7)) : #every 7 days 
    mycursor = mydb.cursor()
    # selcts date of issue and return
    q2 = "SELECT penalty FROM student WHERE stud_id = %s"
    stid = (studid,)
    mycursor.execute(q2, stid)
    pen = mycursor.fetchone()  # fetch only one record
    
    if pen is None or pen[0] is None:
          applied_penalty = 0  # Initialize penalty if none exists
    else:
          applied_penalty = pen[0] 
    applied_penalty +=10
    # update penalty  
    q3 = "UPDATE student SET penalty = %s WHERE stud_id = %s"
    updated = (applied_penalty , studid)
    mycursor.execute(q3, updated)
    mydb.commit()
    print("penalty applied")
    
# penalty(1)
  

        
        
        
        
        
        
        
  
  