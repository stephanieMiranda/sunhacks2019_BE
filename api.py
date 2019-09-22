from flask import Flask, jsonify, request
from flasgger import Swagger
from flasgger import swag_from
import api_doc_specs.specs as const
import json
from shMongoDBLogic import ShMongoDBLogic as db

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/getUser/<user_email>/')
@swag_from(const.user_dict, methods=['GET'])
def getUser(user_email):
    """endpoint returning user information
    ---
 
    """
    result = db.getUserByEmail(user_email)
    print(result)
    return jsonify(result)

@app.route('/productsPost', methods = ['PUT'])
@swag_from(const.products)
def productsPost():
	rv = {"hi" : True}
	print(request.json)
	return jsonify(rv)

def pprint(py_dict):
	print(json.dumps(py_dict, sort_keys=True,indent=4, separators=(',', ': ')))

pprint(const.user_dict)

app.run(debug=True)