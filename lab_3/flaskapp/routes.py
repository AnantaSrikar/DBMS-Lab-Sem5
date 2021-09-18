from flask import jsonify

from flaskapp import app

from dbhandler.sqlhandler import dbh

@app.route("/")
def root():
	return jsonify({"msg": "Welcome to dbAPI!"})

@app.route("/user/register", methods=['POST'])
def add_user():
	print(dbh.add_user('test'))
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