# Deploying model -- Flask, Streamlit and Heroku 


## Project Overview
Simple project using scikit learn to build and serve models via  Flask API or Streamlit and deploy using Heroku. The goal is to create a ML pipeline starting with building model, transforming it to production ready code and then deploying the model via API or via Streamlit.


## Model Overview
The model is constructed fairy simply with selecting only top 10 features and using SVM from scikit learn. If anyone wishes to improve model accuracy, consider adding more features and balancing the target class. As mentioned the purpose of this project is to build the entire ML pipeline from model building to deployment, so I kept the model as simple as I could.



## Running Locally
Modularize local packages with `python setup.py develop` first. 
<br/>
#### streamlit app
For running Streamlit, run the app with `streamlit run app.py` on the localhost 
<br/>
#### Flask API
For running Flask API, set up Flask with `set FLASK_APP = app.py` and run with `python run.py` Flask API doesn't have html template, so I suggest running with Streamlit if anyone wants to play with the app. 


## Testing
Using Tox to automate training and testing model. Using pytest for testing both model and Flask API

