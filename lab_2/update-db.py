"""
	Script to create a new database with tables, in MySQL

	Author: Srikar
"""

import mysql.connector
import os
from getpass import getuser

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

# Changes requested in current lab
mycursor.execute("alter table Student add gender char(1) default 'M';")
mycursor.execute("alter table Student add team char(1);")
mycursor.execute("alter table Student drop column age;")
mycursor.execute("alter table Student add dob date;")
mycursor.execute("alter table Student add yjoin int;")


# To display the values in the way needed
mycursor.execute("ALTER TABLE Student MODIFY dob date AFTER rollno;")
mycursor.execute("ALTER TABLE Student MODIFY yjoin int AFTER dob;")
mycursor.execute("ALTER TABLE Student MODIFY gender char(1) AFTER yjoin;")
mycursor.execute("ALTER TABLE Student MODIFY team char(1) AFTER gender;")

prev_Campus = {
	'names': ["dwayne", "john", "dave", "randy", "kane", "tom"],
	'dob': ['2000-01-09', '2002-03-21', '1999-09-11', '2001-04-28', '2000-11-01', '2000-11-01'],
	'yjoin': [2019, 2019, 2018, 2019, 2018, 2019],
	'team': ['R', 'W', 'A', 'R', 'G', 'W']
}

for i in range(6):
	# print("OwO")
	mycursor.execute(f"""UPDATE Student SET
		dob=STR_TO_DATE('{prev_Campus["dob"][i]}', '%Y-%m-%d'),
		yjoin={prev_Campus["yjoin"][i]},
		team='{prev_Campus["team"][i]}'
		WHERE name LIKE '{prev_Campus["names"][i]}';""")