#! python3

# imports
import os
import logging
import bs4
import requests
import urllib.request

# logging - filename='..\\logs\\xkcd.log', 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def getImage(url) -> str:
    ''' getImage takes a URL for xkcd.com, downloads and saves that image.'''

    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        print('Invalid response status, %s' % (response.status_code))

    # Get soup object to parse the response
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Identify the div that contains the comic, by id='comic' ...
    comicDiv = soup.find('div', {'id':'comic'})

    # Then find the img tag within that div ... 
    comicImg = comicDiv.find('img')

    # Then extract the source attribute ... 
    comicSrc = 'https:' + comicImg['src']

    comicFile = '.\\xkcdImages\\xkcd_' + str(comicNumber) + '.png'

    # Then retrieve the image:
    urllib.request.urlretrieve(comicSrc, comicFile)

def getPreviousPage(url) -> str:
    '''getPreviousPage parses the response from the url to find the 'prev' button
    and return the url to the previous comic. 
    
    Parameters
    ----------
    url : str
    The url of the current page
    
    Returns
    -------
    previousUrl : str
    The url of the previous comic
    '''

    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        print('Invalid response status, %s' % (response.status_code))

    # Get soup object to parse the response
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

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
    getImage(url)
    prev = getPreviousPage(url)
    url = prev
    comicNumber -= 1