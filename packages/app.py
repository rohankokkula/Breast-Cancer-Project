import streamlit as st
import pandas as pd
import time

from model.config import config
from model.processing.data_management import load_pipeline


pipeline_filename = f"{config.PIPELINE_TO_SAVE}.pkl"
model = load_pipeline(filename = pipeline_filename)




def make_prediction(input_data):

    with st.spinner('Making prediction...'):
        time.sleep(3)

    predictions = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)
    return predictions, prediction_proba


def clean_output(prediction):
        if prediction == 'M':
                return 'Malignant'
        else:
                return 'Benign'



def run():
    st.title('Breast Cancer Diagnosis Model')

    concave_points_mean = st.slider('concave points (mean)', 0.0, 0.21, 0.1)
    concave_points_worst = st.slider('concave points (worst)', 0.0, 0.29, 0.1)
    area_worst = st.slider('area (worst)', 185, 4245, 1000)
    perimeter_worst = st.slider('perimeter (worst)',50, 250, 100)
    radius_worst = st.slider('radius (worst)', 8, 36, 20)
    concavity_mean = st.slider('concavity (mean)', 0.0, 0.43, 0.2)
    area_mean = st.slider('area (mean)', 143, 2501, 1000)
    radius_mean = st.slider('radius (mean)', 7, 28, 15)
    area_se = st.slider('area (se)', 7, 542, 200)
    concavity_worst = st.slider('concavity (worst)', 0.0, 1.3, 0.5)
    perimeter_mean = st.slider('perimeter (mean)', 43, 188, 100)



    input_dict = {

                'concave points (mean)': concave_points_mean,
                'concave points (worst)': concave_points_worst,
                'area (worst)': area_worst,
                'perimeter (worst)': perimeter_worst,
                'radius (worst)' : radius_worst,
                'concavity (mean)' : concavity_mean, 
                'area (mean)': area_mean,
                'radius (mean)': radius_mean,
                'area (se)': area_se,
                'concavity (worst)' : concavity_worst,
                'perimeter (mean)': perimeter_mean
        }


    input_df = pd.DataFrame([input_dict])   


    if st.button('Predict'):
        output, proba = make_prediction(input_df)
        output = clean_output(output)
        probability = max(proba[0][0], proba[0][1])

        st.success(f"The predicted result is {output} with probability of {round(probability*100)}%")





    # st.number_inputs('concave points (mean)', min_value = 0, max_value = 0.21)
    # st.number_inputs('concave points (worst)', min_value = 0, max_value = 0.29)
    # st.number_inputs('perimeter (worst)', min_value = 50, max_value = 250)
    # st.number_inputs('perimeter (mean)', min_value = 43, max_value = 188)
    # st.number_inputs('radius (mean)', min_value = 7, max_value = 28)
    # st.number_inputs('radius (worst)', min_value = 8, max_value = 36)





if __name__ == '__main__':

    run()



