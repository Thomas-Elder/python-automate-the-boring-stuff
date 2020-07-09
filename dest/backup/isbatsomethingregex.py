#! python3

import sys
import re

text = str(sys.argv[1:])
print(text)

batpattern = re.compile(r'Bat(mobile|man|copter)')
match = batpattern.findall(text)

print(match)

if match:
    for i in match:
        print(i)
else:
    print('Bat not found')