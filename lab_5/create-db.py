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

# Try to connect to university_profile
try:
	mydb = connectDB("university_profile")

except mysql.connector.errors.ProgrammingError:
	print("DB not existing, run previous scripts to make one :)")

mycursor = mydb.cursor()

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
	for i in range(len(marks_sem1['rollnos'])):
		query = "INSERT INTO marks_sem1 VALUES (%s, %s, %s, %s, %s, %s);"
		values = (marks_sem1['rollnos'][i], marks_sem1['math'][i], marks_sem1['sci'][i], marks_sem1['eng'][i], marks_sem1['social'][i], marks_sem1['sports'][i])
		mycursor.execute(query, values)
	
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")
	

except mysql.connector.errors.IntegrityError:
	print("Looks like you already created the table marks_sem1")

except Exception as e:
	print(f"Something bad happened :( => {e}")

mycursor.execute("""CREATE TABLE IF NOT EXISTS faculty (
	name VARCHAR(20),
	fid CHAR(4) NOT NULL PRIMARY KEY,
	subject VARCHAR(20)
	);
	""")

try:
	for i in range(len(faculty['names'])):
		query = "INSERT INTO faculty VALUES (%s, %s, %s);"
		values = (faculty['names'][i], faculty['fid'][i], faculty['subject'][i])
		mycursor.execute(query, values)

	mydb.commit()
	print(mycursor.rowcount, "record inserted.")

except mysql.connector.errors.IntegrityError:
	print("Looks like you already created the table faculty")

except Exception as e:
	print(f"Something bad happened :( => {e}")

# Check for candidate keys
mycursor.execute("""CREATE TABLE IF NOT EXISTS sem1 (
	subj_id CHAR(4) NOT NULL PRIMARY KEY,
	subject VARCHAR(20),
	fid CHAR(4),
	cap INT,
	campus INT,
	CONSTRAINT fk_fid FOREIGN KEY (fid) REFERENCES faculty(fid),
	CONSTRAINT fk_campus FOREIGN KEY (campus) REFERENCES Campus(cid)
	);
	""")

try:
	for i in range(len(sem1['subj_id'])):
		query = "INSERT INTO sem1 VALUES (%s, %s, %s, %s, %s);"
		values = (sem1['subj_id'][i], sem1['subject'][i], sem1['fid'][i], sem1['cap'][i], sem1['campus'][i])
		mycursor.execute(query, values)

	mydb.commit()
	print(mycursor.rowcount, "record inserted.")

except mysql.connector.errors.IntegrityError:
	print("Looks like you already created the table sem1!")

except Exception as e:
	print(f"Something bad happened :( => {e}")

mydb.close()