import requests

URL = 'https://www.amazon.in/Test-Exclusive-750/dp/B07DJCYBVK/ref=sr_1_4?dchild=1&keywords=oneplus+8+pro&qid=1613290429&sr=8-4'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'}

page= requests.get(URL,headers=headers)