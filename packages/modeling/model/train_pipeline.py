from model.processing.data_management import load_data, save_pipeline
from model.pipeline import model_pipeline
from model.config import config



def run_training() -> None:
	data = load_data(filename ='train.csv')
	features = data[config.FEATURES]
	target = data[config.TARGET]
	model_pipeline.fit(features, target)
	save_pipeline(pipeline_to_persist = model_pipeline)


if __name__ == "__main__":
	run_training()