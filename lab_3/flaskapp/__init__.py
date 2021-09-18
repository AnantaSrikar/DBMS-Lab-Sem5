"""
	Initialisation of the API
	
	Author: Srikar
"""

from flask import Flask

app = Flask(__name__)

from flaskapp import routes