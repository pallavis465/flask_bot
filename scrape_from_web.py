from urllib.error import URLError
import requests
import wget as wget
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse

my_urls = ['https://www.dell.com/support/home/us/en/04/product-support/product/dell-1u-rackmount-led-console/docs']
links = []
names = []
for url in my_urls:
    resp = requests.get(url)
    soup = bs(resp.text,'lxml')
    og = soup.find("meta",  property="og:url")
    base = urlparse(url)
    for i,link in enumerate (soup.find_all('a')):
        current_link = link.get('href')
        if current_link.endswith('en-us.pdf'):
            links.append(current_link)
            names.append(soup.select('a')[i].attrs['href'])

myset=set(links)
newlinks=list(myset)
names_urls = zip(names, newlinks)

for link in newlinks:
    print(link)
print("**")
for name, link in names_urls:
    try:
        print (name)
        print(link)
        wget.download(link)
        res = requests.get(link)
        pdf = open("pdfs/" + name, 'wb')
        pdf.write(res.read())
        pdf.close()
    except URLError as e:
        if e.code == 404:
            pass

'''for link in newlinks:
    try:
        wget.download(link)
    except URLError as e:
        if e.code == 404:
            pass'''

'''import requests
from bs4 import BeautifulSoup as bs
import urllib2


_ANO = '2013/'
_MES = '01/'
_MATERIAS = 'matematica/'
_CONTEXT = 'wp-content/uploads/' + _ANO + _MES
_URL = 'http://www.desconversa.com.br/' + _MATERIAS + _CONTEXT

# functional
r = requests.get(_URL)
soup = bs(r.text)
urls = []
names = []
for i, link in enumerate(soup.findAll('a')):
    _FULLURL = _URL + link.get('href')
    if _FULLURL.endswith('.pdf'):
        urls.append(_FULLURL)
        names.append(soup.select('a')[i].attrs['href'])

names_urls = zip(names, urls)

for name, url in names_urls:
    print(url)
    rq = urllib2.Request(url)
    res = urllib2.urlopen(rq)
    pdf = open("pdfs/" + name, 'wb')
    pdf.write(res.read())
    pdf.close()'''


