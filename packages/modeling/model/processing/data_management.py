import pandas as pd
from model.config import config
import joblib
from sklearn.pipeline import Pipeline



def load_data(*, filename: str) -> pd.DataFrame:
	_data = pd.read_csv(f"{config.DATASET_DIR}/{filename}")
	return _data



def save_pipeline(*, pipeline_to_persist) -> None:
	save_file_name = f"{config.PIPELINE_TO_SAVE}.pkl"
	save_path = config.TRAINED_MODEL_DIR/save_file_name
	joblib.dump(pipeline_to_persist, save_path)




def load_pipeline(*,filename: str ) -> Pipeline:
	file_path = config.TRAINED_MODEL_DIR/filename
	trained_model = joblib.load(filename = file_path)

	return trained_model


