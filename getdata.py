
import requests
import re
import json
from bs4 import BeautifulSoup

baseurl = "https://deliveroo.co.uk" #specific url not written heer
    

headers = {'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWbKit/537.36(KHTML, like Gecko) Chrome/74.0.3729169 Safari/537.36'
} #use this to avoid scraper being detected

t = "https://deliveroo.co.uk" # see line 7

x = "https://deliveroo.co.uk" #see line 7

r = requests.get(x)
soup = BeautifulSoup(r.content, 'lxml')

productlist= soup.find_all('span', class_="MenuItemCard-d6db654c8b51be41 MenuItemCard-a7b546f3e376be7f")
pricelist = soup.find_all('span', class_= "ccl-649204f2a8e630fd ccl-98a86d2cf2dd0739 ccl-5009081e3e0d6b1f ccl-08c109442f3e666d")

imagelink = soup.find_all('div', class_= "ccl-a897ba3fd642670d ccl-92294f995a389ac9")

extracted_text = []
prods = [element.get_text() for element in productlist]

print(prods)


soup = BeautifulSoup(r.text, 'html.parser')

div_element = soup.find('div', class_='MenuItemCard-ff35664fd9aa5264')
style_attr = div_element.get('style')

pattern = r'"blocks":\[(.*?)\]'
matches = re.findall(pattern, r.text)
#print(matches)
# Extract the URLs from the first occurrence of "blocks"
if len(matches) > 0:
    urls = re.findall(r'"url":"(https?://[^"]+)"', matches[1])


dataobject = {}

for i,x in zip(prods,urls):
    dataobject[i] = x

print(dataobject)


    


