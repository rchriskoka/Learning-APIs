#The goal of our simple flask application is to help users to manage income and expenses. 

from flask import Flask, jsonify, request 

app = Flask(__name__)

incomes = [ 
	{'description':'salary', 'amount':5000}
]

#Endpoint to handle HTTP GET request to return incomes
@app.route('/incomes')
def get_incomes():
	return json.dumps(incomes)

	
#Endpoint to handle HTTP POST requests to add new incomes
@app.route('/incomes', methods=['POST'])
def add_income():
	incomes.append(request.get_json())
	return '', 204


