from flask import Blueprint, request, jsonify
from model.predict import make_prediction
from model.processing.data_management import load_data
from model.config import config
import json

prediction_app = Blueprint('prediction_app', __name__)

_data = load_data(filename = 'test.csv')
features = _data[config.FEATURES][0:1]


@prediction_app.route('/test', methods = ['GET'])
def test():
	if request.method == 'GET':
		return 'living the dream!'



@prediction_app.route('/predict', methods =['POST'])
def predict():
	if request.method == 'POST':
		json_data = request.get_json()
		results = make_prediction(input_data = json_data)
		predictions = results.get('predictions')[0]

		return jsonify({'predictions': predictions})





# # make_prediction function accepts json and pass into model by converting it to dataframe

# @prediction_app.route('/values', methods = ['GET'])
# def predict():
# 	if request.method == 'GET':
# 		data = features.to_json(orient = 'records')
# 		results = make_prediction(input_data = data)
# 		predictions = results.get('predictions')[0]

# 		return predictions
