import requests


endpoint = "http://localhost:8000/api/products/"

data= {
    'title':78,
    # 'content':'Post request is Sucessfull',
    # 'price': 20
}
get_response = requests.post(endpoint,data)

print(get_response.json())
