#! python3

#TODO: imports
import re, pyperclip

#TODO: regex for phone numbers
phoneRegex = re.compile(r''' 
(                            # We group the whole thing in one, to make accessing it easier 
(((\d\d\d)|(\(\d\d\d\))))?   # OPTIONAL Area code without parentheses OR Area code with parentheses
(-|\s)                       # separator
(\d\d\d)                     # first 3 digits of the phone number
-                            # separator
(\d\d\d\d)                   # second 4 digits of the phone number
(((ext(\.)?\s)|x)(\d{2,5}))? # OPTIONAL extentions
)
''', re.VERBOSE)

#TODO: regex for emails
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+             # Name, could include some symbols, so char class
@                           # separator @ symbol
[a-zA-Z0-9_.+]+             # Domain
''', re.VERBOSE)

#TODO: get text from clipboard
phoneAndEmailData = pyperclip.paste()

#TODO: extract phone/emails
extractedPhoneNumberTuples = phoneRegex.findall(phoneAndEmailData)
extractedPhoneNumbers = []
for number in extractedPhoneNumberTuples:
    extractedPhoneNumbers.append(number[0])

extractedEmails = emailRegex.findall(phoneAndEmailData)

#TODO: copy data back to clipboard
results = '\n'.join(extractedPhoneNumbers) + '\n' + '\n'.join(extractedEmails)
pyperclip.copy(results)