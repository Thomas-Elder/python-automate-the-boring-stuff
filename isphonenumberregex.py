#! python3
import sys
import re

phonepattern = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match = phonepattern.search(sys.argv[1])

if match == None:
    print('Text entered is not a phone number')
else:
    print('Area code is %s and number is %s' % (match.group(1), match.group(2)))