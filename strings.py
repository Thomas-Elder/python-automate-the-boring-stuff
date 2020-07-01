spam = 'Hello World!'
print(spam.upper())
print(spam.lower())

# both false because there is a mix of chars
print(spam.isupper())
print(spam.islower())

# is true, as the result of spam.upper() is all upper case
print(spam.upper().isupper())

# you can call the methods on literals
print('Hello'.upper())

# True, it's in title case
print(spam.istitle())

# False, due to the whitespace
print(spam.isalpha())

# False, due to the whitespace
print(spam.isalnum())

otherspam = 'HelloWorld'

#Both True
print(otherspam.isalpha())
print(otherspam.isalnum())

commaspam = ', '.join(spam)
print(commaspam)
#H, e, l, l, o,  , W, o, r, l, d, !

splitspam = spam.split('l')
print(splitspam)
#['He', '', 'o Wor', 'd!']

spam = 'Hello there!'
print(spam.replace('e', 'XYZ'))
# HXYZllo thXYZrXYZ!

# String formatting
name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'

invitation = 'Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.'

print(invitation)
# Hello Alice, you are invited to a party at Main Street at 6 pm. Please bring turnips.  

invitation = "Hello %s, you are invited to a party at %s at %s. Please bring %s" % (name, place, time, food)
print(invitation)
# Hello Alice, you are invited to a party at Main Street at 6 pm. Please bring turnips.  