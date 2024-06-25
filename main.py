import requests
import json

print(json.loads(requests.get("http://numbersapi.com/random/trivia").text))
