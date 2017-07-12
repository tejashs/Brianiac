import requests
url = 'http://localhost:5000/predict/flower'
files = {'flowerImage': ('file', open('/home/kiranupadya/Documents/cloudml-samples/flowers/0.jpg', 'rb'), 'image/jpg', {'Expires': '0'})}
headers = {'Content-type': 'application/json'}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text) 
