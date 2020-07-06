#! python3
import re

#
# A regex pattern can just be a simple string to match
br1 = re.compile(r'The adventures of batman and his batmobile')
match = br1.search('The adventures of batman and his batmobile')
print(match)
#<re.Match object; span=(0, 42), match='The adventures of batman and his batmobile'>

match = br1.search('The adventures of batwoman and her batcopter')
print(match)
#None

#
# Or we can use groups and pipes to specify possible alternative matches
br2 = re.compile(r'The adventures of bat(man|woman) and (his|her) bat(mobile|copter)')
match = br2.search('The adventures of batwoman and her batcopter')
print(match)
#<re.Match object; span=(0, 44), match='The adventures of batwoman and her batcopter'>

match = br2.search('The adventures of batman and his batmobile')
print(match)
#<re.Match object; span=(0, 42), match='The adventures of batman and his batmobile'>

#
# We can use ? to specify that a group occurs once or not at all
br3 = re.compile(r'The adventures of bat(wo)?man and (his|her) bat(mobile|copter)')
match = br3.search('The adventures of batwoman and her batcopter')
print(match)
# <re.Match object; span=(0, 44), match='The adventures of batwoman and her batcopter'>

#
# We can use * to specify that a group occurs many times or not at all
br4 = re.compile(r'The adventures of bat(wo)*man and (his|her) bat(mobile|copter)')
match = br4.search('The adventures of batwowowoman and her batcopter')
print(match)
# <re.Match object; span=(0, 48), match='The adventures of batwowowoman and her batcopter'>

#
# We can use + to specify that a group occurs 1 or more times
br5 = re.compile(r'The adventures of bat(wo)+man and (his|her) bat(mobile|copter)')
match = br5.search('The adventures of batwoman and her batcopter')
print(match)
# <re.Match object; span=(0, 44), match='The adventures of batwoman and her batcopter'>

match = br5.search('The adventures of batman and his batmobile')
print(match)
# None because wo doesn't appear in this string

#
# We can use {x} to specify that a pattern appear x times 
br6 = re.compile(r'The adventures of bat(wo){3}man and (his|her) bat(mobile|copter)')
match = br6.search('The adventures of batwowowoman and her batcopter')
print(match)
# <re.Match object; span=(0, 48), match='The adventures of batwowowoman and her batcopter'>

br6 = re.compile(r'The adventures of bat(wo){3}man and (his|her) bat(mobile|copter)')
match = br6.search('The adventures of batwowoman and her batcopter') # only two wo
print(match)
# None

#
# And we can use {x, y} to specify that a pattern appear x to y times 
br6 = re.compile(r'The adventures of bat(wo){3,5}man and (his|her) bat(mobile|copter)')
match = br6.search('The adventures of batwowowowowoman and her batcopter')
print(match)
# <re.Match object; span=(0, 48), match='The adventures of batwowowowowoman and her batcopter'>

# This would work for batwowowoman, batwowowowoman, and batwowowowowoman
# Just like slicing, we can leave off either number
# {3,} means 3 or more, {,5} means 0 to 5.

# Matching digits
dr1 = re.compile(r'(\d){3,5}')
match = dr1.search('123456789')
print(match)
# <re.Match object; span=(0, 5), match='12345'>
# This is greedy matching, it matches the longest possible string that fits the pattern.
# It also matches the first possible match. 
# For a non-greedy match, you can add a ? after the curly braces
dr2 = re.compile(r'(\d){3,5}?')
match = dr2.search('123456789')
print(match)
# <re.Match object; span=(0, 3), match='123'>

# testing findall.... 
phoneregex = re.compile(r'(\d\d\d)?-(\d\d\d)-(\d\d\d\d)')
results = phoneregex.findall('Phone numbers are 123-123-1234, -123-1234, 123')
print(results)

# More character classes
cc1 = re.compile(r'\d') # matches any numeric value
cc2 = re.compile(r'\D') # matches any non-numeric value
cc3 = re.compile(r'\w') # matches any letter or numeric value, and the underscore character
cc4 = re.compile(r'\W') # matches any non-letter, non-numeric value, and not the underscore character
cc5 = re.compile(r'\s') # matches any space, tab or newline
cc6 = re.compile(r'\S') # matches any character which is not space, tab or newline

# Examples
print(cc1.search('123')) # <re.Match object; span=(0, 1), match='1'>
print(cc1.search('abc')) # None

print(cc2.search('123')) # None
print(cc2.search('abc')) # <re.Match object; span=(0, 1), match='a'>

print(cc3.search('_')) # <re.Match object; span=(0, 1), match='_'>
print(cc3.search('1')) # <re.Match object; span=(0, 1), match='1'>
print(cc3.search('a')) # <re.Match object; span=(0, 1), match='a'>
print(cc3.search('*')) # None

print(cc4.search('*')) # <re.Match object; span=(0, 1), match='*'>
print(cc4.search('a')) # None

print(cc5.search(' ')) # <re.Match object; span=(0, 1), match=' '>
print(cc5.search('\t')) # <re.Match object; span=(0, 1), match='\t'>
print(cc5.search('''
''')) # <re.Match object; span=(0, 1), match='\n'>
print(cc5.search('1')) # None

print(cc6.search(' ')) # None
print(cc6.search('1')) # <re.Match object; span=(0, 1), match='1'>

# Test time
lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 gold rings, 4 calling birds, 3 French hens, 2 turtle doves, And 1 partridge in a pear tree'
giftsregex = re.compile(r'\d+\s\w+')
print(giftsregex.findall(lyrics))

# We can create our own character classes by listing the chars we want between []
cc7 = re.compile(r'[aeoiu]')
print(cc7.findall('Hi how are you?')) # ['i', 'o', 'a', 'e', 'o', 'u']
# [a-z] matches lower case letters
# [A-Z] matches upper case letters

cc8 = re.compile(r'[aeoiu]{2}') # matches two instances of the characters in [] in a row
print(cc8.findall('Robocop eats baby food')) # ['ea', 'oo']

# Adding a caret at the start of the character class, matches every character than ISN'T in the class
cc9 = re.compile(r'[^aeoiu]')
print(cc9.findall('Hi how are you?')) # ['H', ' ', 'h', 'w', ' ', 'r', ' ', 'y', '?']

# Adding caret at the start of the pattern only matches if the pattern is at the start of the string
cc10 = re.compile(r'^Hello')
print(cc10.findall('Hello, how are you?')) # ['Hello']
print(cc10.findall('How are you? Hello')) # None

# Adding a dollar sign at the end of the pattern only matches if it is at the end of the string
cc11 = re.compile(r'you\?$')
print(cc11.findall('Hello, how are you?')) # ['you?']
print(cc11.findall('How are you? Hello')) # None

# Use both caret and dollar sign to match the whole string
cc12 = re.compile(r'^Hello$')
print(cc12.findall('Hello')) # ['Hello']
print(cc12.findall('Hello, how are you?')) # None

# Or perhaps more usefully
cc13 = re.compile(r'^\d+$') # to match only strings completely digits
print(cc13.findall('1235156236126613615')) # ['1235156236126613615']
print(cc13.findall('123515623x126613615')) # None

# The . stands for anything except \n
cc14 = re.compile(r'.at')
print(cc14.findall('The cat in the hat sat on the mat.')) # ['cat', 'hat', 'sat', 'mat']

# Using .* matches pretty much everything, except \n
cc15 = re.compile(r'First name: (.*) Last name: (.*)')
print(cc15.findall('First name: Thomas Last name: Elder')) # [('Thomas', 'Elder')]

# Testing on a slightly more complicated data set? 
names = '''First name: Thomas Last name: Elder
First name: Finlay Last name: Thingo
First name: Jordanna Last name: Doopidoo
First name: Matthew Last name: Allerinor
First name: Trudi Last name: Baddington'''
print(cc15.findall(names)) # [('Thomas', 'Elder'), ('Finlay', 'Thingo'), ('Jordanna', 'Doopidoo'), ('Matthew', 'Allerinor'), ('Trudi', 'Baddington')]

# neat.

# .* is greedy, can be non-greedy by adding ?
string = '<To serve humans> for dinner!>'
cc16 = re.compile(r'<(.*)>')
print(cc16.findall(string)) # ['To serve humans> for dinner!']

cc17 = re.compile(r'<(.*?)>')
print(cc17.findall(string)) # ['To serve humans']

