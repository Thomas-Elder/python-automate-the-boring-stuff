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
#