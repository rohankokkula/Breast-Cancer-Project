# Deploying model -- Flask, Streamlit 


## Project Overview
Simple project using scikit learn to build models and deploy it through Flask API and / or Streamlit. The goal is to create a ML pipeline starting with building model, transforming it to production ready code and then deploying the model via API or via Streamlit.


## Model Overview
I made the model very simple with selecting only top 10 features and using SVM from scikit learn. If anyone wishes to improve model accuracy, consider adding more features and balancing the target class. As mentioned the purpose of this project is to build the entire ML pipeline from model building to deployment, so I kept the model as simple as I could.


## Running
Modularize local packages with `python setup.py develop` first. For running Streamlit, run the app with `streamlit run app.py` on the localhost 
<br/>
For running Flask API, set up Flask with `set FLASK_APP = app.py` and run with `python run.py` Flask API doesn't have html template, so I suggest running with Streamlit if anyone wants to play with the app. 



## Testing
Using Tox to automate training and testing model. Using pytest for testing both model and Flask API

