import sqlite3
#try connecting to db so it doesn't create a new one everytime
try:
    conn  = sqlite3.connect('student.db')
except Error as e:
    print(e)
#establish cursor & connetion
c = conn.cursor()
conn.commit()
c.execute("CREATE TABLE IF NOT EXISTS StudentsAssign2("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "FirstName VARCHAR(25),"
                        "LastName VARCHAR(25),"
                        "GPA REAL,"
                        "Major VARCHAR(10),"
                        "Advisor VARCHAR(25)"
                        ");")
conn.commit()
