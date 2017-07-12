import requests
url = 'https://steam-airfoil-169600.appspot.com/predict/number'
files = {'digitImage': ('file', open('/home/kiranupadya/Documents/digitRecognition/0.jpg', 'rb'), 'image/jpg', {'Expires': '0'})}
headers = {'Content-type': 'application/json'}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

files = {'digitImage': ('file', open('/home/kiranupadya/Documents/digitRecognition/1.jpg', 'rb'), 'image/jpg', {'Expires': '0'})}
headers = {'Content-type': 'application/json'}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

files = {'digitImage': ('file', open('/home/kiranupadya/Documents/digitRecognition/2.jpg', 'rb'), 'image/jpg', {'Expires': '0'})}
headers = {'Content-type': 'application/json'}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

files = {'digitImage': ('file', open('/home/kiranupadya/Documents/digitRecognition/3.jpg', 'rb'), 'image/jpg', {'Expires': '0'})}
headers = {'Content-type': 'application/json'}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

files = {'digitImage': ('file', open('/home/kiranupadya/Documents/digitRecognition/4.jpg', 'rb'), 'image/jpg', {'Expires': '0'})}
headers = {'Content-type': 'application/json'}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

files = {'digitImage': ('file', open('/home/kiranupadya/Documents/digitRecognition/5.jpg', 'rb'), 'image/jpg', {'Expires': '0'})}
headers = {'Content-type': 'application/json'}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

files = {'digitImage': ('file', open('/home/kiranupadya/Documents/digitRecognition/6.jpg', 'rb'), 'image/jpg', {'Expires': '0'})}
headers = {'Content-type': 'application/json'}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

files = {'digitImage': ('file', open('/home/kiranupadya/Documents/digitRecognition/7.jpg', 'rb'), 'image/jpg', {'Expires': '0'})}
headers = {'Content-type': 'application/json'}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

files = {'digitImage': ('file', open('/home/kiranupadya/Documents/digitRecognition/8.jpg', 'rb'), 'image/jpg', {'Expires': '0'})}
headers = {'Content-type': 'application/json'}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

files = {'digitImage': ('file', open('/home/kiranupadya/Documents/digitRecognition/9.jpg', 'rb'), 'image/jpg', {'Expires': '0'})}
headers = {'Content-type': 'application/json'}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
