#! python3
import sys
import re

# \d matches any numerical value
# () can be used to group patterns
# ? specifies that the preceding group appears once or not at all in the pattern
# So the below will match 123-123-1234, and 123-1234
phonepattern = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
match = phonepattern.search(sys.argv[1])

if match == None:
    print('Text entered is not a phone number')
else:
    print('Number is %s' % (match.group()))