#! python3
import sys
import re

print(re.match(r'\d\d\d-\d\d\d-\d\d\d\d', sys.argv[1]).string)