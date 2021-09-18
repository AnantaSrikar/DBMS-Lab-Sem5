"""
	Handling all the mySQL related interactions

	Author: Srikar
"""

from dbhandler import mycursor

class dbh:
	def add_user(username):
		return {"msg" : f"Added {username} to the database!"}
	
	def update_user(username):
		return {"msg" : f"Updated {username} to the database!"}

	def delete_user(username):
		return {"msg" : f"Deleted {username} to the database!"}

	def view_users():
		return {"msg" : "All the users in db!"}