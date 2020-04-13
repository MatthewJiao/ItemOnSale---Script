import requests
import bs4
import lxml
import csv
import smtplib
from email.message import EmailMessage
import imghdr
res = requests.get('https://www.amazon.ca/gp/product/B07SNFDB7J?pf_rd_r=6G0EZX2YTZDEVSCZ4NAK&pf_rd_p=05326fd5-c43e-4948-99b1-a65b129fdd73')
soup = bs4.BeautifulSoup(res.text, 'lxml')
x = '10'
y = '2'
with open('counter.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        y = line
        break

if y[0] == '2':
    csv_file = open('scrape.csv','w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(soup)
    x='1'
    #print("noo") for testing purposes

if y[0] == '1':
    csv_file2 = open('scrape2.csv','w')
    csv_writer2 = csv.writer(csv_file2)
    csv_writer2.writerow(soup)
    x='2'
    #print("yess") for testing purposes


csv_file3 = open('counter.csv','w')
csv_writer3 = csv.writer(csv_file3)
csv_writer3.writerow(x)

with open('scrape.csv', 'r') as t1, open('scrape2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('output.csv', 'w') as outFile:
    csv_writer4 = csv.writer(outFile)
    for line in filetwo:
        if line not in fileone:
            csv_writer4.writerow(line)

z = '21'
m = False
with open('output.csv', 'r') as rea:
    csv_reader5 = csv.reader(rea)

    for line in csv_reader5:
        print(line)
        if line != "":
            m = True

if m:
    print("send email") # for testing purposes

    password = 'password'
    msg = EmailMessage()
    msg['Subject'] = "New Sale Alert"
    msg['From'] = 'email1'
    msg['To'] = 'email2'
    msg.set_content('Amazon.ca has a new sale!')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()





#beep = soup.find('div', class_='span12 widget-span widget-type-raw_jinja hs-blog-header')
#bop = hi.h1.text
#print(bop)

#for hi in soup.find_all('div', class_='name'):
  #  name = hi.a.text
  #  print(name)

#wrapper = soup.find('title')
#attr = wrapper.find('div', class_='score')
#print(soup.prettify())