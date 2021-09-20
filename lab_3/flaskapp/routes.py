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

	# print(dbh.add_user('test'))
	# return jsonify(dbh.add_user(data))
	return jsonify({"msg": "Added user!"})

@app.route("/user/update", methods=['POST'])
def update_user():
	print(dbh.update_user('test'))
	return jsonify({"msg": "Updated user!"})

@app.route("/user/delete", methods=['POST'])
def del_user():
	print(dbh.delete_user('test'))
	return jsonify({"msg": "Deleted user!"})

@app.route("/user/view", methods=['GET'])
def view_users():
	print(dbh.view_users())
	return jsonify({"msg": "See all users!"})