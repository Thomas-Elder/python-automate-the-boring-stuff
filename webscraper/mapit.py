#! python3

# Imports
import webbrowser
import sys
import pyperclip
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

if len(sys.argv) > 1:
    logging.debug('sys.argv > 1, location parameters entered.')
    logging.debug('sys.argv: %s' % (sys.argv))

    location = '+'.join(sys.argv[1:])
    logging.debug('location: %s' % (location))

    webbrowser.open('https://www.google.com.au/maps/place/%s' % (location))

elif pyperclip.paste() == '':
    logging.info('Clipboard is empty')

    clipboard = pyperclip.paste()
    logging.debug(clipboard)

    location = '+'.join(clipboard.split(' '))
    logging.debug(location)

    webbrowser.open('https://www.google.com.au/maps/place/%s' % (location))

else: 
    logging.info('No parameters passed, and nothing on the clipboard.')