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

# Changes requested in current lab for table Student
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
	'name': ["dwayne", "john", "dave", "randy", "kane", "tom"],
	'dob': ['2000-01-09', '2002-03-21', '1999-09-11', '2001-04-28', '2000-11-01', '2000-11-01'],
	'yjoin': [2019, 2019, 2018, 2019, 2018, 2019],
	'team': ['R', 'W', 'A', 'R', 'G', 'W']
}

for i in range(6):
	mycursor.execute(f"""UPDATE Student SET
		dob=STR_TO_DATE('{prev_Campus["dob"][i]}', '%Y-%m-%d'),
		yjoin={prev_Campus["yjoin"][i]},
		team='{prev_Campus["team"][i]}'
		WHERE name LIKE '{prev_Campus["name"][i]}';""")

mydb.commit()

# Extra records
new_students = {
	'name': ["carol", "wanda", "natasha", "gamora", "jean"],
	'rollnos': [7, 21, 52, 34, 46],
	'dob': ['2000-06-19', '2001-08-10', '2001-06-19', '2001-06-19', '2001-06-19'],
	'yjoin': [2018, 2019, 2019, 2018, 2019],
	'team': ['w', 'R', 'A', 'G', 'G'],
	'math': [78, 42, 83, 84, 98],
	'sci': [99, 73, 86, 93, 97],
	'eng': [45, 59, 89, 79, 84],
	'social': [56, 63, 91, 94, 87],
	'sports': [88, 65, 99, 85, 72]
}

for i in range(5):
	mycursor.execute(f"""
		INSERT INTO Student VALUES ('{new_students["name"][i]}',
		{new_students["rollnos"][i]},
		STR_TO_DATE('{prev_Campus["dob"][i]}', '%Y-%m-%d'),
		{new_students["yjoin"][i]},
		'F',
		'{new_students["team"][i]}',
		{new_students["math"][i]},
		{new_students["sci"][i]},
		{new_students["eng"][i]},
		{new_students["social"][i]},
		{new_students["sports"][i]}
		);
	""")

mydb.commit()