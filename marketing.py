
import requests



#using this url to access the api 
url = "https://ml-deploy-fastapi.fly.dev/predict" 


customer = {
  "gender": "male",
  "seniorcitizen": 0,
  "partner": "no",
  "dependents": "yes",
  "phoneservice": "no",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "no",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "yes",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "mailed_check",
  "tenure": 7,
  "monthlycharges": 29.75,
  "totalcharges": 131.9
}

response = requests.post(url, json=customer)
# print("Status Code:", response.status_code)


Churn = response.json()
print(f'Churn {Churn}')


if Churn['porb']>=50:
    print('customer is likely to churn, send promo')
else:
    print('customer is not likely to churn')


