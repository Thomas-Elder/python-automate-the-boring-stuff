#! python3

# imports
import sys
import logging
import requests

# logging
logging.basicConfig(filename='..\\logs\\xkcd.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# ping
url = 'https://xkcd.com/'

repsonse = requests.get(url)

try: 
    repsonse.raise_for_status()

except:
    logging.debug('Request failed, status: %s' % (repsonse.status_code))
