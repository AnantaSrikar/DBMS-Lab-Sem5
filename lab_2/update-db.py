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

mycursor.execute("ALTER TABLE Student ADD gender CHAR(1) DEFAULT 'M';")
mycursor.execute("ALTER TABLE Student ADD team CHAR(1);")
mycursor.execute("ALTER TABLE Student DROP COLUMN age;")
mycursor.execute("ALTER TABLE Student ADD dob DATE;")
mycursor.execute("ALTER TABLE Student ADD yjoin INT;")


# To display the values in the way needed
mycursor.execute("ALTER TABLE Student MODIFY dob DATE AFTER rollno;")
mycursor.execute("ALTER TABLE Student MODIFY yjoin INT AFTER dob;")
mycursor.execute("ALTER TABLE Student MODIFY gender CHAR(1) AFTER yjoin;")
mycursor.execute("ALTER TABLE Student MODIFY team CHAR(1) AFTER gender;")

prev_students = {
	'name': ["dwayne", "john", "dave", "randy", "kane", "tom"],
	'dob': ['2000-01-09', '2002-03-21', '1999-09-11', '2001-04-28', '2000-11-01', '2000-11-01'],
	'yjoin': [2019, 2019, 2018, 2019, 2018, 2019],
	'team': ['R', 'W', 'A', 'R', 'G', 'W']
}

for i in range(6):
	mycursor.execute(f"""UPDATE Student SET
		dob=STR_TO_DATE('{prev_students["dob"][i]}', '%Y-%m-%d'),
		yjoin={prev_students["yjoin"][i]},
		team='{prev_students["team"][i]}'
		WHERE name LIKE '{prev_students["name"][i]}';""")

mydb.commit()

# Extra records
new_students = {
	'name': ["carol", "wanda", "natasha", "gamora", "jean"],
	'rollnos': [7, 21, 52, 34, 46],
	'dob': ['2000-06-19', '2001-08-10', '2001-06-19', '2001-06-19', '2001-06-19'],
	'yjoin': [2018, 2019, 2019, 2018, 2019],
	'team': ['W', 'R', 'A', 'G', 'G'],
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
		STR_TO_DATE('{new_students["dob"][i]}', '%Y-%m-%d'),
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


# Changes requested in current lab for Campus table

mycursor.execute("ALTER TABLE Campus ADD pincode CHAR(6)")

prev_campus = {
	'names': ['mec', 'muc', 'mgt'],
	'pincode': ['500043', '600012', '400076']
}

for i in range(3):
	mycursor.execute(f"""UPDATE Campus SET
		pincode='{prev_campus["pincode"][i]}'
		WHERE name LIKE '{prev_campus["names"][i]}';
	""")

mydb.commit()

mycursor.execute("ALTER TABLE Campus MODIFY pincode CHAR(6) AFTER loc;")

new_campus = {
	'names': ['mdc', 'mdd', 'mvc', 'mbd'],
	'cid': [106, 109, 110, 113],
	'loc': ['pun', 'del', 'vel', 'bgl'],
	'pincode': ['411021', '110001', '631001', '560002'],
	'cap': [1700, 1400, 1400, 800],
	'law': [0, 1, 1, 0],
	'engg': [1, 1, 1, 1],
	'buss': [1, 0, 1, 1]
}

for i in range(4):
	mycursor.execute(f"""INSERT INTO Campus VALUES (
		'{new_campus["names"][i]}',
		{new_campus["cid"][i]},
		'{new_campus["loc"][i]}',
		'{new_campus["pincode"][i]}',
		{new_campus["cap"][i]},
		{new_campus["law"][i]},
		{new_campus["engg"][i]},
		{new_campus["buss"][i]}
	);
	""")

mydb.commit()