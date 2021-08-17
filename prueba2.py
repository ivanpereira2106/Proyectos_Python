import requests
import bs4
res=requests.get('http://10.10.1.212/web/guest/es/websys/webArch/mainFrame.cgi')
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text, 'html.parser')
element=soup.select('#machine > div.mgn-8px-3px.txt-algn-L > div.left > dl:nth-child(3) > dd')
print(element[0].text)
