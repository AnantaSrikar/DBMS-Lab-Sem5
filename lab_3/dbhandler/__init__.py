"""
	Initialising the database handler
	
	Author: Srikar
"""
import mysql.connector
import os
from getpass import getuser

# DB: userDB, table: user_data

hasDB = False
try:
	mydb = mysql.connector.connect(
			host="localhost",
			user=getuser(),
			password=f"{os.environ['SQL_P']}",
			database="userDB"
		)

	hasDB = True

except mysql.connector.errors.ProgrammingError:
	mydb = mysql.connector.connect(
			host="localhost",
			user=getuser(),
			password=f"{os.environ['SQL_P']}",
		)

	mycursor = mydb.cursor()

	mycursor.execute("CREATE DATABASE userDB")

mycursor = mydb.cursor()

if not hasDB:
	mycursor.execute("USE userDB")

mycursor.execute("""CREATE TABLE IF NOT EXISTS user_data (
	name VARCHAR(20) NOT NULL,
	phno INT PRIMARY KEY,
	dob DATE NOT NULL
	);
	""")