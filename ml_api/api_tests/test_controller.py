from model.config import config as model_config
from model.processing.data_management import load_data
import json


def test_test_endpoint_returns_200(flask_test_client):
	# When
	response = flask_test_client.get('/test')

	# Then
	assert response.status_code == 200

def test_predict_end_point_returns_prediction(flask_test_client):
	# Given
	test_data = load_data(filename = 'test.csv')
	test_data = test_data[model_config.FEATURES][0:1]
	test_json= test_data.to_json(orient = 'records')

	# When
	response = flask_test_client.post('/predict', json = test_json)

	# Then
	assert response.status_code == 200
	response_json = json.loads(response.data)
	prediction = response_json['predictions']
	assert prediction == 'B'

