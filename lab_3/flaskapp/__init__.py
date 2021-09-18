"""
	Initialisation of the API
	
	Author: Srikar
"""

from flask import Flask

# TODO: import dbhandler

app = Flask(__name__)

from flaskapp import routes

# TODO: Initialise db