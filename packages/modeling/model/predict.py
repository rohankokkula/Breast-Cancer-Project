import pandas as pd
from model.processing.data_management import load_pipeline, load_data
from model.config import config
from sklearn.metrics import accuracy_score




pipeline_name = f"{config.PIPELINE_TO_SAVE}.pkl"
model_pipeline = load_pipeline(filename = pipeline_name)



def make_prediction(*, input_data):
	data = pd.read_json(input_data)
	pred = model_pipeline.predict(data)
	results = {"predictions" : pred}

	return results



if __name__ == '__main__':
	data = load_data(filename = 'test.csv')
	features = data[config.FEATURES]
	y_pred = model_pipeline.predict(features)
	y_test = data[config.TARGET]
	print(accuracy_score(y_test, y_pred))
	print(y_pred)

	