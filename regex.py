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

