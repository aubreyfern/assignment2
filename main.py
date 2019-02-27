#prints out all data in db
def displayAll():
    c.execute("SELECT * FROM StudentsAssign2")
    table = c.fetchall()
    for x in table:
        print(x)
    return;

#prints data in table given fetchall data
def printRows(data):
    if(data!=[]):
        for x in data:
            print(x)
    else:
        print("Does not exist")

#take user input & add student to db
def createStudent():
    #get user input
    firstName = input("Enter in student first name: ").lower()
    lastName = input("Enter in student last name:").lower()
    major = input("Enter in major:").upper()
    advisor = input("Enter in advisor:").lower()
    gpa = float(input("Enter in GPA:"))
    #if user enters num for name,major or advisor break
    if(firstName.isdigit()or lastName.isdigit() or major.isdigit() or advisor.isdigit()):
        print("Invalid Input")
    #if user entered gpa is out of range
    elif(gpa>4.0or gpa <0.0):
        print("Invalid Input-GPA out of Range")
    #add to db
    else:
        c.execute("INSERT into StudentsAssign2(FirstName,LastName,Major,Advisor,GPA)"
        "VALUES(?,?,?,?,?)",(firstName,lastName,major,advisor,gpa))
        conn.commit()

#check is student exists on db by id
def realStudent(stuId):
    #is user input is a number not a letter, check db for id
    if(stuId.isdigit()):
        c.execute("select id from StudentsAssign2 where id = "+stuId)
        stu = c.fetchall()
        #if id is not in db
        if(stu==[]):
            print("Student Doesn't Exist")
            return False;
        else:
            return True;
    #user input was not a number
    else:
        print("Invalid Response-NOT INT")

#update student major or advisor
def updateStudent():
    search = input("Enter the ID of student you'd like to update: ")
    #check if student is in db by id
    if(realStudent(search)):
        option  = input("Would you want to update major(m) or advisor(a):").lower()
        #update major
        if(option == 'm'):
            newMajor = input("Change major to:").upper()
            #query to update major
            c.execute("update StudentsAssign2 set Major = '{0}' where id='{1}'".format(newMajor,search))
            conn.commit()
        #update advisor
        elif(option =='a'):
            newAdvisor = input("Change Advisor to:").lower()
            #query to update advisor
            c.execute("update StudentsAssign2 set Advisor = '{0}' where id='{1}'".format(newMajor,search))
            conn.commit()
        #if user did not enter m or a
        else:
            print("Invalid Entry")

#delete student from db
def deleteStudent():
    search = input("Enter the ID of the student you'd like to delete:")
    #check if student is in db
    if(realStudent(search)):
        #query to delete
        c.execute("delete from StudentsAssign2 where id = {0}".format(search))
        conn.commit()

#search in column if a value exists
def searchFor(col,val):
    c.execute(("select {0} from StudentsAssign2 where {0} = '{1}'").format(col,val))
    data = c.fetchall()
    if (data == []):
        print("Does not Exist")
        return False
    #exists in db
    else:
        return True

#search by major,advisor or gpa master
def searchBy():
    option = input("Would you like to search by Major(m), Advisor(a), or GPA (g): ")
    option.lower()
    #search by major
    if(option=='m'):
        optionMajor = input("Search Major:").upper()
        #check if major is in db
        if(searchFor('Major',optionMajor)):
            c.execute("select * from StudentsAssign2 where Major = '{0}'".format(optionMajor))
            majorResult = c.fetchall()
            printRows(majorResult)
    #search by advisor
    elif(option=='a'):
        optionAdvisor = input("Search Advisor:").lower()
        if(searchFor('Advisor',optionAdvisor)):
            c.execute("select * from StudentsAssign2 where Advisor = '{0}'".format(optionAdvisor))
            advisorResult = c.fetchall()
            printRows(advisorResult)
    #seach by gpa
    elif(option == 'g'):
        optionGpa = input("Search GPA:")
        if(searchFor('GPA',optionGpa)):
            c.execute("select * from StudentsAssign2 where GPA = '{0}'".format(optionGpa))
            gpaResults = c.fetchall()
            print(gpaResults)

import sqlite3
import numbers
from student import Student

#try connecting to database so it doesn't create a new one everytime
try:
    conn  = sqlite3.connect('student.db')
except Error as e:
    print(e)

c = conn.cursor()
conn.commit()

while(True):
    print("\nMenu")
    print("1:Display all students")
    print("2:Create student")
    print("3:Update student")
    print("4:Delete student")
    print("5:Search student")
    print("6:Exit")

    choice = input("\nEnter an Option:")

    if(choice == '1'):
        displayAll()
    elif(choice =='2'):
        createStudent()
    elif(choice =='3'):
        updateStudent()
    elif(choice=='4'):
        deleteStudent()
    elif(choice=='5'):
        searchBy()
    elif(choice=='6'):
        break
