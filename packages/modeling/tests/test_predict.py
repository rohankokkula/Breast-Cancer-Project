from model.processing.data_management import load_data
from model.config import config
from model.predict import make_prediction




def test_make_single_prediction():
	# Given
	test_data = load_data(filename = 'test.csv')
	single_test = test_data[config.FEATURES][0:1]
	single_test_json = single_test.to_json(orient = 'records')

	# When
	subject = make_prediction(input_data = single_test_json)

	# Then
	assert subject is not None
	assert subject['predictions'] == 'B'


def test_entire_prediction():
	# Given
	test_data = load_data(filename = 'test.csv')
	test_data = test_data[config.FEATURES]
	data_length = len(test_data)
	test_data_json = test_data.to_json(orient = 'records')

	# When
	subject = make_prediction(input_data = test_data_json)
	predictions = subject['predictions']

	# Then
	assert subject is not None
	assert len(predictions) == data_length
