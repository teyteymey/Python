import webbrowser
import requests

s = requests.Session()
#webbrowser.open('https://google.es')

r = s.get('https://tmb.cat')
print(r.headers)
print(r.request.headers)
