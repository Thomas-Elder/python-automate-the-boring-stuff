#! python3

# imports
import requests
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

url = 'https://automatetheboringstuff.com/files/rj.txt'

response = requests.get(url)

try:
    response.raise_for_status()
    file = open('RomeoAndJuliet.txt', 'wb')
    
    for chunk in response.iter_content(1000):
        file.write(chunk)
    
    file.close()

except:
    print('Bad url')

    
badResponse = requests.get('https://automatetheboringstuff.com/files/jibberish.txt')

try:
    badResponse.raise_for_status()
    file = open('Jibberish.txt', 'wb')
    
    for chunk in response.iter_content(1000):
        file.write(chunk)
    
    file.close()

except:
    print('Bad url')