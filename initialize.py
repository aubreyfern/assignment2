import sqlite3
#try connecting to db so it doesn't create a new one everytime
try:
    conn  = sqlite3.connect('student.db')
except Error as e:
    print(e)

#establish cursor & connetion 
c = conn.cursor()
conn.commit()
