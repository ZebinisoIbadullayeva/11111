import requests

data = {
    'jshr':"1265241"
}

f = open('dg64ej3cjekc6hk.psw','rb')
files = {'fayl': open('dg64ej3cjekc6hk.psw', 'rb')}
rs = requests.post(url='http://127.0.0.1:8000/check/',data=data,files=files)
print(rs.text)