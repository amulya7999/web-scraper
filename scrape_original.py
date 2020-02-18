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
rollno=input("enter roll no")
enter = int(input('enter subject code'))
for x in range(3):
    number=int(rollno)
    number = number + 1
    rollno = str(number)
    data={'mbstatus':'SEARCH','htno':rollno,'Submit.x':'32','Submit.y':'14'}
    res=c.post(url,data=data)
    s = BeautifulSoup(res.content, 'html.parser')
    print(rollno)
    name = s.find_all('table')[0].find_all('tr')[6].find_all('td')[1].get_text()
    print(name)
#title=s.find_all('title')[0].get_text()
#print(title)
#subtitle=s.find_all('p')[0].get_text()
#print(subtitle)
#date=s.find_all('p')[1].get_text()
#print(date)
#subtitle2=s.find_all('td')[2].get_text()
#print(subtitle2)
    for i in range(8, 13, 1):
        subject = s.find_all('table')[1].find_all('tr')[i].find_all('td')[0].get_text()
        if int(subject) != enter:
            continue
        print(subject)
        grade = s.find_all('table')[1].find_all('tr')[i].find_all('td')[3].get_text()
        print(int(grade))
        gradez = s.find_all('table')[1].find_all('tr')[i].find_all('td')[4].get_text()
        print(gradez)
        z=i
sbname = s.find_all('table')[1].find_all('tr')[z].find_all('td')[1].get_text()
print(sbname)
credit =s.find_all('table')[1].find_all('tr')[z].find_all('td')[2].get_text()
print(credit)
