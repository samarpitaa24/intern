'''Problem 1: Student Management System
Create a program to manage student information for a class. Implement the following features:
Store student details like name, age, and marks in a dictionary where the key is the student's name and the value is another dictionary with age and marks.
Allow the user to add new students, update details of existing students, and display all student details.
Use if-else conditions to evaluate the student's grade based on their marks and display it (e.g., A, B, C, D, or F).
The program should continue to accept inputs until the user chooses to exit.'''

student = {
    "Raya" : { "age" : 20 , "marks" : 29} ,
    "Riya" : { "age" : 20 , "marks" : 25} ,
    "Rashi" : { "age" : 20 , "marks" : 24} ,
}


stud_records = int(input("enter no. of students you want to insert records of : "))

for i in range(0,stud_records+1) :
    stud_name = input("enter name : ")
    stud_age = int(input("enter age : "))
    stud_marks = int(input("enter age : "))
    student[stud_name] = {"age" : stud_age , "marks" : stud_marks}
    print("record inserted")
    
stud_update = input("enter the name of student who's record you want to update : ")
update_what = input("update age or marks : ")

if update_what == "age":
    new_age= int(input("enter age : "))
    student.get(stud_update)
    student.update( {"age" : new_age})
    print("age updated")
