import mysql.connector
import os

Students = {
	'names': ["dwayne", "john", "dave", "randy", "kane", "tom"],
	'rollnos': [33, 58, 27, 56, 11, 50],
	'ages': [21, 18, 22, 19, 22, 21],
	'math': [98, 70, 54, 69, 86, 76],
	'sci': [94, 87, 68, 75, 95, 84],
	'eng': [91, 77, 98, 65, 52, 62],
	'social': [96, 98, 96, 67, 57, 74],
	'sports': [55, 67, 77, 98, 73, 81]
}

mydb = mysql.connector.connect(
	host="localhost",
	user="srikar",
	password=f"{os.environ['SQL_P']}",
	database="university_profile"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS Student (
	name CHAR(20),
	rollno INT NOT NULL PRIMARY KEY,
	age INT,
	math INT,
	sci INT,
	eng INT,
	social INT,
	sports INT
	);
	""")

try:
	for i in range(6):
		query = "INSERT INTO Student VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
		values = (Students['names'][i], Students['rollnos'][i], Students['ages'][i], Students['math'][i], Students['sci'][i], Students['eng'][i], Students['social'][i], Students['sports'][i])
		mycursor.execute(query, values)
	
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")
	

except mysql.connector.errors.IntegrityError:
	print("Looks like you already created the table")

except Exception as e:
	print(f"Something bad happened :( => {e}")

mycursor.execute("""CREATE TABLE IF NOT EXISTS Campus (
	name CHAR(20),
	cid INT NOT NULL PRIMARY KEY,
	loc CHAR(20),
	cap INT,
	law BOOLEAN,
	engg BOOLEAN,
	buss BOOLEAN
	);
	""")

Campus = {
	'names': ["mec", "muc", "mgt"],
	'cid': [101, 104, 107],
	'loc': ['hyd', 'mad', 'bom'],
	'cap': [1000, 2000, 1500],
	'law': [1, 0, 1],
	'engg': [1, 1, 0],
	'buss': [1, 1, 1]
}

try:
	for i in range(3):
		query = "INSERT INTO Campus VALUES (%s, %s, %s, %s, %s, %s, %s);"
		values = (Campus['names'][i], Campus['cid'][i], Campus['loc'][i], Campus['cap'][i], Campus['law'][i], Campus['engg'][i], Campus['buss'][i])
		mycursor.execute(query, values)

	mydb.commit()
	print(mycursor.rowcount, "record inserted.")

except mysql.connector.errors.IntegrityError:
	print("Looks like you already created the table")

except Exception as e:
	print(f"Something bad happened :( => {e}")

mydb.close()