#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.com/MyDigitalSSD-480GB-512GB-Bullet-Proof/dp/B00N0UQ99S")

content = request.content
soup = BeautifulSoup(content, "html.parser")

product_title = soup.find("span", {"id":"productTitle"})
title_str = product_title.text.strip()

product_price = soup.find("span", {"id":"priceblock_ourprice"})

print(title_str[0:33] + " : " + product_price.text.strip())


