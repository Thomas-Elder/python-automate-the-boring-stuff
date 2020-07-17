#! python3

# imports
import os
import logging
import bs4
import requests
import urllib.request

# logging - filename='..\\logs\\xkcd.log', 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def getImage(soup):  
    # Identify the div that contains the comic, by id='comic' ...
    comicDiv = soup.find('div', {'id':'comic'})

    # Then find the img tag within that div ... 
    comicImg = comicDiv.find('img')

    # Then extract the source attribute ... 
    comicSrc = 'https:' + comicImg['src']

    comicFile = '.\\xkcdImages\\xkcd_' + str(comicNumber) + '.png'

    # Then retrieve the image:
    urllib.request.urlretrieve(comicSrc, comicFile)

def getPreviousPage(soup):
    # Use this response to find the 'prev' button, and return that url, so it can be passed to the next getImage call
    
    # Get the ul for the nav, using the class
    previous = soup.find('a', {'rel':'prev'})

    previousUrl = StartingUrl + previous['href']

    return previousUrl

# ping
StartingUrl = 'https://xkcd.com'
comicNumber = 2333

if not os.path.exists('.\\xkcdImages'):
    os.mkdir('.\\xkcdImages')

while comicNumber > 2330:
    url = StartingUrl
    response = requests.get(url) 
    
    try:
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        getImage(soup)

        prev = getPreviousPage(soup)

    except:
        print('Invalid response status, %s' % (response.status_code))

    # Here I need a new request for the previous comic

    url = prev
    comicNumber -= 1