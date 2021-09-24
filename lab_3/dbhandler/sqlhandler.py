"""
	Handling all the mySQL related interactions

	Author: Srikar
"""

# TODO: make table name dynamic
# TODO: Fix phone number

from dbhandler import mycursor
from dbhandler import mydb

class dbh:
	def add_user(user_data):

		query = "INSERT INTO user_data VALUES (%s, %s, STR_TO_DATE(%s, '%Y-%m-%d'));"
		values = (user_data['name'], user_data['phno'], user_data['dob'])

		mycursor.execute(query, values)
		mydb.commit()
		
		return {"msg" : f"Added {user_data['name']} to the database!"}
	
	def update_user(user_data):
		query = "UPDATE user_data SET name=%s WHERE phno=%s;"
		values = (user_data['name'], user_data['phno'])

		mycursor.execute(query, values)
		mydb.commit()

		return {"msg" : f"Updated {user_data['name']} in the database!"}

	def delete_user(user_data):

		# TODO: dynamically delete user depending on the data provided

		mycursor.execute(f"DELETE FROM user_data WHERE phno={user_data['phno']};")

		mydb.commit()

		return {"msg" : f"Deleted user with phno {user_data['phno']} from the database!"}

	def view_users():

		mycursor.execute("SELECT * FROM user_data")

		table_info = mycursor.fetchall()

		data = {}

		for row in table_info:
			data[row[1]] = {}
			
			data[row[1]]['name'] = row[0]
			data[row[1]]['dob'] = row[2]

		return data