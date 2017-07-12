import requests
url = 'http://localhost:5000/predict/number'
files = {'digitImage': ('file', open('/home/kiranupadya/Documents/digitRecognition/0.jpg', 'rb'), 'image/jpg', {'Expires': '0'})}
headers = {'Content-type': 'application/json'}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
