from flask import Flask, jsonify
from flasgger import Swagger
from flasgger import swag_from
import api_doc_specs.specs as const
import json

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/colors/<palette>/')
@swag_from(const.specs_dict, methods=['GET'])
def colors(palette):
    """Example endpoint returning a list of colors by palette
    ---
 
    """
    all_colors = {
        'cmyk': ['cian', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue'],
        'hi_mom': ['derp', 'derp']
    }
    if palette == 'all':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return jsonify(result)

@app.route('/productsPost', methods = ['POST'])
@swag_from(const.products, validation=True)
def productsPost():
	rv = {"hi" : True}
	return jsonify(rv)

def pprint(py_dict):
	print(json.dumps(py_dict, sort_keys=True,indent=4, separators=(',', ': ')))

pprint(const.specs_dict)

app.run(debug=True)