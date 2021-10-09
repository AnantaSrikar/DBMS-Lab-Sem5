"""
	Script to update existing tables, in MySQL

	Author: Srikar
"""

import mysql.connector
import os
from getpass import getuser

# Data to be modified for table Student
cid_data = {
	'name': ['dwayne', 'john', 'dave', 'randy', 'kane', 'tom', 'carol', 'wanda', 'natasha', 'gamora', 'jean'],
	'cid': [109, 101, 110, 104, 104, 101, 113, 107, 109, 109, 110]
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

try:
	for i in range(len(cid_data['name'])):
		query = "UPDATE Student SET cid=%s WHERE name like %s;"
		values = (cid_data['cid'][i], cid_data['name'][i])
		mycursor.execute(query, values)

	mydb.commit()

except Exception as e:
	print(f"Something bad happened :( => {e}")

mydb.close()