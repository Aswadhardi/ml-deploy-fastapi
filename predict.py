import pickle 

from typing import Dict,Any
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

 
from pydantic import BaseModel, Field, conint, confloat
from typing import Literal

class Customer(BaseModel):
    gender: Literal['male', 'female']
    seniorcitizen: conint(ge=0, le=1)
    partner: Literal['yes', 'no']
    dependents: Literal['yes', 'no']
    phoneservice: Literal['yes', 'no']
    multiplelines: Literal['no', 'yes', 'no_phone_service']
    internetservice: Literal['dsl', 'fiber_optic', 'no']
    onlinesecurity: Literal['yes', 'no', 'no_internet_service']
    onlinebackup: Literal['yes', 'no', 'no_internet_service']
    deviceprotection: Literal['yes', 'no', 'no_internet_service']
    techsupport: Literal['yes', 'no', 'no_internet_service']
    streamingtv: Literal['yes', 'no', 'no_internet_service']
    streamingmovies: Literal['yes', 'no', 'no_internet_service']
    contract: Literal['month-to-month', 'one_year', 'two_year']
    paperlessbilling: Literal['yes', 'no']
    paymentmethod: Literal[
        'electronic_check',
        'mailed_check',
        'bank_transfer_(automatic)',
        'credit_card_(automatic)'
    ]
    tenure: conint(ge=0, le=72)
    monthlycharges: confloat(ge=18.25, le=118.75)
    totalcharges: confloat(ge=0.0, le=8684.8)
    


class PredictResponse(BaseModel):
    churn_rate: float = Field(..., description="Predicted churn probability as a percentage")
    churn: bool = Field(..., description="True if churn_rate ≥ 50%, else False")


app = FastAPI(title='churn-prediction')

def load_model(filename):
    with open (filename, 'rb') as f_in:
        pipeline = pickle.load(f_in)
    
    print(f'Model loaded from {filename}')   
    return pipeline

pipeline = load_model('model.bin')



def predict_single(customer):
    results = pipeline.predict_proba(customer)[0,1]
    return round(results*100,2)


@app.post('/predict')
def predict(customer:Customer ) -> PredictResponse:
    prob = predict_single(customer.model_dump())
    
    return PredictResponse(
        churn_rate = prob,
        churn = bool(prob >= 50)
    )

    
if __name__ =='__main__':
    uvicorn.run(app,host='0.0.0.0')
