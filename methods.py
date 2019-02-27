import sqlite3
import initialize
#prints out all data in db
def displayAll():
    initialize.c.execute("SELECT * FROM StudentsAssign2")
    table = initialize.c.fetchall()
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
    elif(gpa>4.0 or gpa <0.0):
        print("Invalid Input-GPA out of Range")
    #add to db
    else:
        initialize.c.execute("INSERT into StudentsAssign2(FirstName,LastName,Major,Advisor,GPA)"
        "VALUES(?,?,?,?,?)",(firstName,lastName,major,advisor,gpa))
        initialize.conn.commit()

#check is student exists on db by id
def realStudent(stuId):
    #is user input is a number not a letter, check db for id
    if(stuId.isdigit()):
        initialize.c.execute("select id from StudentsAssign2 where id = "+stuId)
        stu = initialize.c.fetchall()
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
            initialize.c.execute("update StudentsAssign2 set Major = '{0}' where id='{1}'".format(newMajor,search))
            initialize.conn.commit()
        #update advisor
        elif(option =='a'):
            newAdvisor = input("Change Advisor to:").lower()
            #query to update advisor
            initialize.c.execute("update StudentsAssign2 set Advisor = '{0}' where id='{1}'".format(newAdvisor,search))
            initialize.conn.commit()
        #if user did not enter m or a
        else:
            print("Invalid Entry")

#delete student from db
def deleteStudent():
    search = input("Enter the ID of the student you'd like to delete:")
    #check if student is in db
    if(realStudent(search)):
        #query to delete
        initialize.c.execute("delete from StudentsAssign2 where id = {0}".format(search))
        initialize.conn.commit()

#search in column if a value exists
def searchFor(col,val):
    initialize.c.execute(("select {0} from StudentsAssign2 where {0} = '{1}'").format(col,val))
    data = initialize.c.fetchall()
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
            initialize.c.execute("select * from StudentsAssign2 where Major = '{0}'".format(optionMajor))
            majorResult = initialize.c.fetchall()
            printRows(majorResult)
    #search by advisor
    elif(option=='a'):
        optionAdvisor = input("Search Advisor:").lower()
        if(searchFor('Advisor',optionAdvisor)):
            initialize.c.execute("select * from StudentsAssign2 where Advisor = '{0}'".format(optionAdvisor))
            advisorResult = initialize.c.fetchall()
            printRows(advisorResult)
    #seach by gpa
    elif(option == 'g'):
        optionGpa = input("Search GPA:")
        if(searchFor('GPA',optionGpa)):
            initialize.c.execute("select * from StudentsAssign2 where GPA = '{0}'".format(optionGpa))
            gpaResults = initialize.c.fetchall()
            print(gpaResults)
