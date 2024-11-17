# import the necessary packages
import requests


# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = r"http://enidai.ru/json"
DATA = "Как у тебя дела?"

# load the input image and construct the payload for the request

r = requests.post(KERAS_REST_API_URL, json={"data":DATA}).json()
print(r["data"])
