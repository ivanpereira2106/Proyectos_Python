import requests
import bs4
res=requests.get('http://www.hospitaluniversitario.edu.py/listado-de-medicos-y-horarios/')
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text, 'html.parser')
universitario=soup.select('#medicom-layout > section > div.bg-color > div')
print(universitario[0].text)
