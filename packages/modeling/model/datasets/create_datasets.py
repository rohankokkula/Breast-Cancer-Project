from model.config import config
import pandas as pd
import numpy as np


PATH = config.DATASET_DIR
FILE_NAME = 'breast_cancer_data.csv'


_data = pd.read_csv(f"{PATH}/{FILE_NAME}")
split_size = np.ceil(len(_data)*0.8).astype(int)
train_data = _data.iloc[:split_size]
test_data = _data.iloc[split_size:]

train_data.to_csv(f"{PATH}/train.csv")
test_data.to_csv(f"{PATH}/test.csv")