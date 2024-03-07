import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
# endpoint = "http://127.0.0.1:8000/api/room/1"
endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint, json={'query':"hellow world"})
get_response = requests.get(endpoint, params={'abc': 123 }, json={'query':"hellow world"})
# get_response = requests.get(endpoint, data={'query':"hellow world"})
# get_response = requests.get(endpoint)
# print(get_response.headers)
# print(get_response.text)
print(get_response.json())
# print(get_response.json()['message'])
# print(get_response.status_code)

 
 
