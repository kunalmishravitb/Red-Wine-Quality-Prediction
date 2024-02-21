# 🍷🍇 Red Wine Quality Prediction Project

## Overview
This project aims to predict the quality of red wine based on various physicochemical features using machine learning techniques. The quality of wine is a crucial aspect for producers and consumers alike, and being able to predict it accurately can streamline production processes and guide consumer choices.
We utilize a dataset containing various features related to red wine samples. Each wine in the dataset is assigned a quality score between 0 and 10. Our goal is to build classification models that can accurately predict whether a particular red wine is of “good quality” or not based on these features.


## About Dataset - Taken from Kaggle
**Context:**

The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine.

These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones).


**Content:**

Input variables (based on physicochemical tests):
1. fixed acidity
2. volatile acidity
3. citric acid
4. residual sugar
5. chlorides
6. free sulfur dioxide
7. total sulfur dioxide
8. density
9. pH
10. sulphates
11. alcohol
Output variable (based on sensory data):
12. quality (score between 0 and 10)


## Workflows

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity 
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py


## Steps to Run
💿 Installing
1. Environment setup
```
conda create -p venv python==3.9.18 -y
```
```
conda activate venv/
````
OR
```
conda create -p venv python==3.9.18 ipykernel -y
```
```
conda activate venv/
````
2. Install Requirements and setup
```
pip install -r requirements.txt
```
3. Run Application
```
python app.py
```
4. Open your browser and hit the url given below
```
http://127.0.0.1:8080/
```
```
http://127.0.0.1:8080/train
```
```
http://127.0.0.1:8080/predict
```



🔧 Built with
- flask
- Python 3.9
- Machine learning
- Jupyter Notebook
- Scikit learn
- 🏦 Industrial Use Cases

