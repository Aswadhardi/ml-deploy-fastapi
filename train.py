#!/usr/bin/env python
# coding: utf-8

# This is a starter notebook for an updated module 5 of ML Zoomcamp
# 
# The code is based on the modules 3 and 4. We use the same dataset: [telco customer churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
import pickle 

import pandas as pd
import numpy as np
import sklearn  

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline


print(f'pandas=={pd.__version__}')
print(f'numpy=={np.__version__}')
print(f'sklearn=={sklearn.__version__}')


def load_data():

    data_url = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv'

    df = pd.read_csv(data_url)

    df.columns = df.columns.str.lower().str.replace(' ', '_')

    categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

    for c in categorical_columns:
        df[c] = df[c].str.lower().str.replace(' ', '_')

    df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
    df.totalcharges = df.totalcharges.fillna(0)
    df.churn = (df.churn == 'yes').astype(int) 
    
    return df


def train_model(df):
    y_train = df.churn

    numerical = ['tenure', 'monthlycharges', 'totalcharges']
    categorical = [
        'gender',
        'seniorcitizen',
        'partner',
        'dependents',
        'phoneservice',
        'multiplelines',
        'internetservice',
        'onlinesecurity',
        'onlinebackup',
        'deviceprotection',
        'techsupport',
        'streamingtv',
        'streamingmovies',
        'contract',
        'paperlessbilling',
        'paymentmethod',
    ]

    pipeline = make_pipeline(
        DictVectorizer(),LogisticRegression(solver='liblinear')
    )

    train_dict = df[categorical + numerical].to_dict(orient='records')
    pipeline.fit(train_dict,y_train)
    
    return pipeline


def save_model(filename, model):
    with open (filename, 'wb')  as f_out: 
        pickle.dump(pipeline, f_out)

    print(f'Model saved to {filename}')

df = load_data()
pipeline = train_model(df)
save_model('model.bin', pipeline)

 
 





def load_model(filename,model):
    with open (filename, 'rb') as f_in:
        pipeline = pickle.load(f_in)
    
    print(f'Model loaded from {filename}')   


customer = {'gender': 'male',
 'seniorcitizen': 0,
 'partner': 'no',
 'dependents': 'yes',
 'phoneservice': 'no',
 'multiplelines': 'no_phone_service',
 'internetservice': 'dsl',
 'onlinesecurity': 'no',
 'onlinebackup': 'yes',
 'deviceprotection': 'no',
 'techsupport': 'no',
 'streamingtv': 'yes',
 'streamingmovies': 'no',
 'contract': 'month-to-month',
 'paperlessbilling': 'yes',
 'paymentmethod': 'mailed_check',
 'tenure': 7,
 'monthlycharges': 29.75,
 'totalcharges': 131.9} 


def predict(customer):
    churn = pipeline.predict_proba(customer)[0,1]
    print(f'Probability of churn is {round(churn * 100,2)}%')


    if churn>=0.5:
        print('Initiate mitigating action')
    else:
        print('Do nothing')
    