#Aubrey Fernando
#CPSC 408
#Assignment2
import sqlite3
import numbers
#import from other classes
import methods
import initialize
from student import Student

#looop menu until exit
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
        methods.displayAll()
    elif(choice =='2'):
        methods.createStudent()
    elif(choice =='3'):
        methods.updateStudent()
    elif(choice=='4'):
        methods.deleteStudent()
    elif(choice=='5'):
        methods.searchBy()
    elif(choice=='6'):
        break
