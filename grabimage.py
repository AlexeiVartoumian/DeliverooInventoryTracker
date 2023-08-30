
import requests

from bs4 import BeautifulSoup

baseurl = "https://deliveroo.co.uk" # this is a prototype and wont include the specific url I am targeting
    

headers = {'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWbKit/537.36(KHTML, like Gecko) Chrome/74.0.3729169 Safari/537.36'
}

t = "https://deliveroo.co.uk/menu/***********************************" # hard-coding the specific url as asterisks , this is hust to show prof of concept
r = requests.get( t)

soup = BeautifulSoup(r.content, 'lxml')

productlist= soup.find_all('span', class_="MenuItemCard-d6db654c8b51be41 MenuItemCard-a7b546f3e376be7f")
pricelist = soup.find_all('span', class_= "ccl-649204f2a8e630fd ccl-98a86d2cf2dd0739 ccl-5009081e3e0d6b1f ccl-08c109442f3e666d")


images = []
play = str(soup)


names = []


def sliding(window,array): # wrote this for fun! accepts the json input and turns into a string. since it followed a particualr pattern just followed the pattern with a sliding window. this is where I grab the specific urls where the images are hosted
    l = 0
    r = 9
    
    start = '"image":{'
 
    while r < len(window):
        sliding = window[l:r]
        if sliding == start:
            curstring = ""
            littleleft = r-2
            while r < len(window) and window[littleleft:r+1] != '"},':
                curstring+= window[r]
                r+=1
                l+=1
                littleleft+=1
            array.append(curstring)
            
        else:
            r+=1
            l+=1
    return names
sliding(play,names)

print(names)

res = []

for i in names:
    x = i.split('"')
    res.append(x)

