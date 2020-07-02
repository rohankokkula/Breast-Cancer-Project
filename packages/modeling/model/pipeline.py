from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC


model_pipeline = Pipeline([

		('scaler', MinMaxScaler()),
		('model', SVC(C = 3, probability = True))
		
	])