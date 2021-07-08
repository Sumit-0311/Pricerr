import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Test-Exclusive_2020_1152-Multi-3GB-Storage/dp/B089MS8VYG/ref=sr_1_3?dchild=1&keywords=redmi+note+10+pro&qid=1625425472&s=electronics&sr=1-3'

yourPrice = 16.000

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'}


def checkPrice():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    decprice = price.replace(",", ".")
    converted_price = float(decprice[2:8])

    print(title.strip())
    print(converted_price)

    if(converted_price > yourPrice):
        sendMail()
    else:
        print('\nPrice has not dropped below ' + str(yourPrice))


def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    userName = ''
    password = ''
    toMailID = ''

    server.login(userName, password)
    subject = 'Price is down'
    body = 'Check the Amazon Link ASAP: ' + URL

    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail(userName, toMailID, msg)
    print("Email Sent Successfully!!")

    server.quit()


while(True):
    checkPrice()
    time.sleep(86400)
