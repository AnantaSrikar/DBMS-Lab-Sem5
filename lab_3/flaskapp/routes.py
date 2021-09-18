from flask import jsonify

from flaskapp import app

@app.route("/")
def root():
	return jsonify({"msg": "Hello world!"})