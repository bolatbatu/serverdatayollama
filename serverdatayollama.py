from requests import put, get
put('http://192.168.1.108:5000/todo2', data={'data': 'Batuhan Bolat'}).json()