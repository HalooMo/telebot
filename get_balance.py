import requests
import json

url = 'https://neuro-texter.ru/api/balance'
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer your_token'
}

response = requests.request('GET', url, headers=headers)
response.json()