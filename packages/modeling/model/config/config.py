import pathlib
import model
import pandas as pd

PACKAGE_ROOT = pathlib.Path(model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_model'
DATASET_DIR = PACKAGE_ROOT / 'datasets'

PIPELINE_NAME = 'breast_cancer_model'
PIPELINE_TO_SAVE = f"{PIPELINE_NAME}.output"


TARGET = 'diagnosis'

FEATURES = ['concave points_mean', 'concave points_worst', 'area_worst',
       		'perimeter_worst', 'radius_worst', 'concavity_mean', 'area_mean',
       		'radius_mean', 'area_se', 'concavity_worst', 'perimeter_mean']


       		



