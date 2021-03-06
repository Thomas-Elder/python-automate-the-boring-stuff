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
    ''' getImage downloads and saves an xkcd comic.
    
    getImage requests the page at the given url, parses that html for the comic, 
    then downloads the image src and saves it to a file.

    Parameters
    ----------
    url : str
    The url of the page to retrieve the comic from

    comicNumber: int
    A number used to create the filename the comic is saved as
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

    # I found one comic that isn't on the page as an img, so we'll check for None, and 
    # only attempt to dl/save the img if it exists.
    if comicImg != None:
    
        # Then extract the source attribute ... 
        comicSrc = 'https:' + comicImg['src']

        comicFile = '.\\xkcdImages\\xkcd_' + str(comicNumber) + '.png'

        # Then retrieve the image:
        urllib.request.urlretrieve(comicSrc, comicFile)

def getPreviousPage(url: str) -> str:
    '''getPreviousPage takes an xkcd url and returns the url of the prev comic.
    
    It parses the response from the url to find the 'prev' button and returns the url 
    to the previous comic. 
    
    Parameters
    ----------
    url : str
    The url of the current page
    
    Returns
    -------
    previousUrl : str
    The url of the previous comic
    Returns None if the previous comic is # (prev is # on comic 1)
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
url = 'https://xkcd.com'
comicNumber = 2334

if not os.path.exists('.\\xkcdImages'):
    os.mkdir('.\\xkcdImages')

while url != None:
    getImage(url, comicNumber)
    url = getPreviousPage(url)
    comicNumber -= 1