#! python3

# imports
import os
import logging
import bs4
import requests
import urllib.request

# logging
logging.basicConfig(filename='..\\logs\\xkcd.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# ping
url = 'https://xkcd.com/'
comicNumber = 2333

if not os.path.exists('.\\xkcdImages'):
    os.mkdir('.\\xkcdImages')

while comicNumber > 2332:
    response = requests.get(url) 
    
    try:
        response.raise_for_status()

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

        # This works for one image, now I need to change the url to the previous image, 
        # continually until we're all out of images. 

    except:
        print('Invalid response status, %s' % (response.status_code))

    comicNumber -= 1