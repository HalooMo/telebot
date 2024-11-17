import requests
import json


def get_article(task_list):
    for i in task_list:
        url = f'https://neuro-texter.ru/api/task/{i}'
        headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer sk-dWeO690tl9i7biSg9vyXCLsuW'
}

        response = requests.request('GET', url, headers=headers)
        yield response.json()['text']

