from requests import put, ge
put('http://192.168.1.108:5000/todo2', data={'data': 'Batuhan Bolat'}).json()          #Bu komut sayesinde 192.168.1.108 adresin 5000 portlu adresindeki siteye todo2 adlı eklentiyle Batuhan Bolat datasını gönderdik.
