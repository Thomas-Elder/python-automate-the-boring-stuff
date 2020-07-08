#! python3

import re

emailRegex = re.compile(r'''
\w+@ # match some word characters succeded by an @
\w+ # match some more word chars
\. # followed by a dot
\w+ # followed by more word chars
\.? # optionally followed by a dot
\w+ # and more \w chars, to handle test@gmail.net.au 
''', re.VERBOSE)

string = 'tasdf@asd.com afasfa@asd.net.au blah@blah poo.poo.com'

results = emailRegex.findall(string)

print(results)