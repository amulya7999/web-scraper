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
    print(rollno)
    s = BeautifulSoup(res.content, 'html.parser')
#title=s.find_all('title')[0].get_text()
#print(title)
#subtitle=s.find_all('p')[0].get_text()
#print(subtitle)
#date=s.find_all('p')[1].get_text()
#print(date)
#subtitle2=s.find_all('td')[2].get_text()
#print(subtitle2)
    for i in (8,13):
        subject = int(s.find_all('table')[1].find_all('tr')[i].find_all('td')[0].get_text())
        if subject == enter:
            continue
        continue
        print(subject)
    sbname = s.find_all('table')[1].find_all('tr')[i].find_all('td')[1].get_text()
    name = s.find_all('table')[1].find_all('tr')[1].find_all('td')[1].get_text()
    credit =  float(s.find_all('table')[1].find_all('tr')[i].find_all('td')[2].get_text())
    grade =  int(s.find_all('table')[1].find_all('tr')[i].find_all('td')[3].get_text())
    gradez = s.find_all('table')[1].find_all('tr')[i].find_all('td')[4].get_text()  
    print(grade)
    print(gradez)
    print(subject)
    print(name)
print(sbname)
    #print(credit)
    


