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

while comicNumber > 0:
    comicUrl = url + str(comicNumber)

    logging.debug('Retrieving image from: %s' % (comicUrl))
    urllib.request.urlretrieve(comicUrl)
    comicNumber -= 1