import requests
from bs4 import BeautifulSoup

url="https://www.osmania.ac.in/res07/20190318.jsp"

headers={
	# 'url':'https://www.osmania.ac.in/res07/20190318.jsp',
	'Connection': 'close',
	'Content-Type': 'text/html;charset=ISO-8859-1',
	'Date': 'Mon, 24 Jun 2019 07:04:43 GMT',
	'Server': 'Apache/2.2.15 (CentOS)',
	'Transfer-Encoding': 'chunked'
}

c=requests.Session()


rollno="245318737090"
data={'mbstatus':'SEARCH','htno':rollno,'Submit.x':'32','Submit.y':'14'}
res=c.post(url,data=data)
s = BeautifulSoup(res.content)
print(s)