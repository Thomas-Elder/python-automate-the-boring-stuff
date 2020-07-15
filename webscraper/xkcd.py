#! python3

# imports
import os
import logging
import urllib.request

# logging
logging.basicConfig(filename='..\\logs\\xkcd.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# ping
url = 'https://xkcd.com/'
comicNumber = 2332

if not os.path.exists('.\\xkcdImages'):
    os.mkdir('.\\xkcdImages')

while comicNumber > 2300:
    comicUrl = url + str(comicNumber)
    comicFile = '.\\xkcdImages\\xkcd_' + str(comicNumber) + '.png'

    logging.debug('Retrieving image from: %s' % (comicUrl))

    # Ok so this gets me the pages the comic is on, but I need to access the actual image source...
    #
    #urllib.request.urlretrieve(comicUrl, comicFile)
    comicNumber -= 1