import mysql.connector
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rootroot",
  database='vithack'
)
print(mydb)


'''
#creates db
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
'''

'''
#creates table
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE data (ref_id int AUTO_INCREMENT, url VARCHAR(500),highlight varchar(500),PRIMARY KEY (ref_id))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)'''

mycursor = mydb.cursor()

 

#insert url from where you want to scrape data
urlname="https://www.aljazeera.com"
html=Request(urlname, headers={'User-Agent': 'Chrome'})
html = urlopen(html).read()
soup = BeautifulSoup(html, 'lxml')



for link in soup.find_all('a',attrs={'href': re.compile("/")}):
    x=link.get('href')
    if(x[-4:]==".cms" or urlname=="https://www.dnaindia.com" or urlname=="https://www.reuters.com" or urlname=="https://www.aljazeera.com"):
            if(x[:4]=="http"):
                print(x)
                head=x.replace("/",":")
                headfinal=head.replace("-"," ")
                print(headfinal) 
                print(" ")
                q = 'INSERT INTO data (url,highlight) VALUES ("'+x+'","'+headfinal+'")'
                mycursor.execute(q)
            else:
                y=str(urlname+x)
                print(y)
                headline=x.replace("/",":")
                headfinal=headline.replace("-"," ")
                print(headfinal)
                print(" ")
                q = 'INSERT INTO data (url,highlight) VALUES ("'+y+'","'+headfinal+'")'
                mycursor.execute(q)
             

    elif(x[-5:]==".html" and x[:4]=="http"):
        y=str(x)
        print(y)
        r=(y.replace(urlname,""))
        s=(r.replace("/",":"))
        headf=s.replace("-"," ")
        print(headf)
        print(" ")
        
         
        q = 'INSERT INTO data (url,highlight) VALUES ("'+y+'","'+headf+'")'
        mycursor.execute(q)
        
   

mydb.commit()




