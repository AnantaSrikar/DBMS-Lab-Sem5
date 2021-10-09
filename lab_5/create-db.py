"""
	Script to create a new database with tables, in MySQL

	Author: Srikar
"""

import mysql.connector
import os
from getpass import getuser

# Initial data for table marks_sem1
marks_sem1 = {
	'rollnos': [7, 11, 21, 27, 33, 34, 46, 50, 52, 56, 58],
	'math': [78, 86, 42, 54, 98, 84, 98, 76, 83, 69, 70],
	'sci': [99, 95, 73, 68, 94, 93, 97, 84, 86, 75, 87],
	'eng': [45, 52, 59, 98, 91, 79, 84, 62, 89, 65, 77],
	'social': [56, 57, 63, 96, 96, 94, 87, 74, 91, 67, 98],
	'sports': [88, 73, 65, 77, 55, 85, 72, 81, 99, 98, 67]
}

# Initial data for table faculty
faculty = {
	'names': ["kakashi", "guy", "kurenai"],
	'fid': ["4003", "5002", "5038"],
	'subject': ["math", "sports", "eng"]
}

# Initial data for the table sem1
sem1 = {
	'subj_id': ["101", "102", "105"],
	'subject': ["math", "sports", "eng"],
	'fid': ["4003", "5002", "5038"],
	'cap': [60, 70, 60],
	'campus': [101, 101, 104]
}

# Connect to given db
def connectDB(dbName):
	mydb = mysql.connector.connect(
		host="localhost",
		user=getuser(),
		password=f"{os.environ['SQL_P']}",
		database="university_profile"
	)
	return mydb

hasDB = False

# Try to connect to university_profile
try:
	mydb = connectDB("university_profile")
	hasDB = True

# Database doesn't exist, make one
except mysql.connector.errors.ProgrammingError:
	mydb = mysql.connector.connect(
		host="localhost",
		user=getuser(),
		password=f"{os.environ['SQL_P']}"
		)

	mycursor = mydb.cursor()

	mycursor.execute("CREATE DATABASE university_profile")

mycursor = mydb.cursor()

# Connect to db if not connected
if not hasDB:
	mycursor.execute("USE university_profile")

mycursor.execute("""CREATE TABLE IF NOT EXISTS marks_sem1 (
	rollno INT NOT NULL PRIMARY KEY,
	math INT,
	sci INT,
	eng INT,
	social INT,
	sports INT
	);
	""")

try:
	for i in range(6):
		query = "INSERT INTO marks_sem1 VALUES (%s, %s, %s, %s, %s, %s);"
		values = (marks_sem1['rollnos'][i], marks_sem1['math'][i], marks_sem1['sci'][i], marks_sem1['eng'][i], marks_sem1['social'][i], marks_sem1['sports'][i])
		mycursor.execute(query, values)
	
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")
	

except mysql.connector.errors.IntegrityError:
	print("Looks like you already created the table")

except Exception as e:
	print(f"Something bad happened :( => {e}")

mycursor.execute("""CREATE TABLE IF NOT EXISTS faculty (
	name VARCHAR(20),
	fid CHAR(4) NOT NULLPRIMARY KEY,
	subject VARCHAR(20)
	);
	""")

try:
	for i in range(3):
		query = "INSERT INTO faculty VALUES (%s, %s, %s);"
		values = (faculty['names'][i], faculty['fid'][i], faculty['subject'][i])
		mycursor.execute(query, values)

	mydb.commit()
	print(mycursor.rowcount, "record inserted.")

except mysql.connector.errors.IntegrityError:
	print("Looks like you already created the table faculty")

except Exception as e:
	print(f"Something bad happened :( => {e}")


mycursor.execute("""CREATE TABLE IF NOT EXISTS sem1 (
	name VARCHAR(20),
	fid CHAR(4) NOT NULLPRIMARY KEY,
	subject VARCHAR(20)
	);
	""")

try:
	for i in range(3):
		query = "INSERT INTO faculty VALUES (%s, %s, %s);"
		values = (faculty['names'][i], faculty['fid'][i], faculty['subject'][i])
		mycursor.execute(query, values)

	mydb.commit()
	print(mycursor.rowcount, "record inserted.")

except mysql.connector.errors.IntegrityError:
	print("Looks like you already created the table faculty")

except Exception as e:
	print(f"Something bad happened :( => {e}")

mydb.close()