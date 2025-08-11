

# import requests

# url = 'http://localhost:8000/predict'

# customer = {
#   "gender": "male",
#   "seniorcitizen": 0,
#   "partner": "no",
#   "dependents": "yes",
#   "phoneservice": "no",
#   "multiplelines": "no_phone_service",
#   "internetservice": "dsl",
#   "onlinesecurity": "no",
#   "onlinebackup": "yes",
#   "deviceprotection": "no",
#   "techsupport": "no",
#   "streamingtv": "yes",
#   "streamingmovies": "no",
#   "contract": "month-to-month",
#   "paperlessbilling": "yes",
#   "paymentmethod": "mailed_check",
#   "tenure": 7,
#   "monthlycharges": 29.75,
#   "totalcharges": 131.9
# }

# response = requests.post(url, json=customer)
# print("Status Code:", response.status_code)
# print("Headers:", response.headers)
# print("Raw Text:", response.text)


# Churn = response.json()
# print(f'Churn {Churn}')


# if Churn['porb']>=50:
#     print('customer is likely to churn, send promo')
# else:
#     print('customer is not likely to churn')

import requests

url = "http://localhost:8000/predict"
payload = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "yes",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 9,
    "monthlycharges": 29.85,
    "totalcharges": 39.85
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
