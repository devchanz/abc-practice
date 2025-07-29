# 07-json.
import json
import requests

url = 'https://pyhub.kr/melon/20231204.json'

response = requests.get(url) # GET방식 요청에 대한 응답 
print(response)

json_string: str = response.text
response_obj = json.loads(json_string)
print(type(response_obj))

for song in response_obj:
    print(song['곡명'], song['가수'])