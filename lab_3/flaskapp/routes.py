"""
	All the routes for application

	Author: Srikar
"""
from flask import jsonify, request

from flaskapp import app

from dbhandler.sqlhandler import dbh

@app.route("/")
def root():
	return jsonify({"msg": "Welcome to dbAPI!"})

@app.route("/user/register", methods=['POST'])
def add_user():
	
	data_keys = ['name', 'phno', 'dob']

	data = request.get_json()

	if(len(data.keys()) != 3):
		return jsonify({'msg': 'Incorrect JSON format sent!'})

	for key in data_keys:
		if key not in data.keys():
			return jsonify({'msg': 'Incorrect JSON format sent!'})

	return jsonify(dbh.add_user(data))

@app.route("/user/update", methods=['POST'])
def update_user():

	data = request.get_json()

	try:
		return jsonify(dbh.update_user(data))
	
	except Exception as e:
		print(e)
		return jsonify({"msg" : "Failed to update the user!"})

@app.route("/user/delete", methods=['POST'])
def del_user():

	data = request.get_json()

	try:
		return jsonify(dbh.delete_user(data))

	except Except as e:
		print(e)
		return jsonify({"msg" : "Failed to delete the user!"})

@app.route("/user/view", methods=['GET'])
def view_users():
	return jsonify(dbh.view_users())