#Task 1: Create database using SQLite
##Install & load sqlite3
import sqlite3


## Connecting to sqlite and Creating connection object

conn=sqlite3.connect("INSTRUCTOR.db")

## cursor object
cur_Obj= conn.cursor()

#Task 2: Create a table in the database¶
## Drop the table if already exists.
cur_Obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")

query1="""CREATE TABLE IF NOT EXISTS INSTRUCTOR
        (ID INTEGER PRIMARY KEY NOT NULL,
        FNAME VARCHAR(20),
        LNAME VARCHAR(20),
        CITY VARCHAR(20),
        CCODE CHAR(2));"""
print("Table created sucsessfully");
cur_Obj.execute(query1)


#Task 3: Insert a single row of data into the table
#Inserting single row
cur_Obj.execute("""INSERT INTO INSTRUCTOR
                VALUES(1,'Vidya','Geetha','Cherthala',49) """)
#Inserting more than one raw of data

cur_Obj.execute("""INSERT INTO INSTRUCTOR VALUES
                (2,'Kishor', 'Ravikumar','Kerala',50),
                (3,'Nila', 'Kishor','Scotland', 51),
                (4, 'Nadal', 'Kishor','Scotland',52)""")


#Retrieve all data we inserted into the INSTRUCTOR table.
cur_Obj.execute("SELECT * FROM INSTRUCTOR")
print("All data from INSTRUCTOR table are:")
rows=cur_Obj.fetchall()
for row in rows:
 print (row)
 
 #Retrieve First 2 rows of  data we inserted into the INSTRUCTOR table.
cur_Obj.execute("SELECT * FROM INSTRUCTOR")
rows=cur_Obj.fetchmany(2)
print("The first 2 rows from the INSTRUCTOR table are:")
for row in rows:
 print(row)
 
 
#Fetch only FNAME from the table
cur_Obj.execute("SELECT FNAME FROM INSTRUCTOR")
print("The First Names from the table INSTRUCTOR are:")
rows = cur_Obj.fetchall()
for row in rows:
        print(row)
#write and execute an update statement that changes the Rav's CITY to MOOSETOWN
cur_Obj.execute("""UPDATE  INSTRUCTOR 
                SET CITY= 'LinlithgowCity'
                WHERE FNAME='Vidya' """)
print("The updated data :")
cur_Obj.execute("SELECT * FROM INSTRUCTOR")
rows = cur_Obj.fetchmany(1)
for row in rows:
        print (row)
        
#Close the connection
conn.close