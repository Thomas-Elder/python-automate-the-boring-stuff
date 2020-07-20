#! python3

# imports
import os
import logging
import bs4
import requests
import urllib.request

# logging - filename='..\\logs\\xkcd.log', 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def getImage(url: str, comicNumber: int):
    ''' getImage takes a URL for xkcd.com, downloads and saves that image.
    
    Parameters
    ----------
    url : str
    The url of the page to retrieve the comic from
    '''

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

def getPreviousPage(url: str) -> str:
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

    if previous['href'] == '#':
        return None
    else:
        return 'https://xkcd.com' + previous['href']

# ping
url = 'https://xkcd.com/2'
comicNumber = 2

if not os.path.exists('.\\xkcdImages'):
    os.mkdir('.\\xkcdImages')

while url != None:
    getImage(url, comicNumber)
    url = getPreviousPage(url)
    comicNumber -= 1