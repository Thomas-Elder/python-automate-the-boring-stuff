#! python3

import shelve

# "A "shelf" is a persistent, dictionary-like object."
# You can open it like a file, add to it like a dictionary.
shelfFile = shelve.open('myShelf')
shelfFile['exercises'] = ['snatch', 'clean and jerk', 'front squat', 'push press']

print(shelfFile['exercises']) # ['snatch', 'clean and jerk', 'front squat', 'push press']
shelfFile.close()

# You can access the keys from the shelf
shelfFile = shelve.open('myShelf')
print(list(shelfFile.keys())) # ['exercises']
shelfFile.close()

# You can access the values from the shelf
shelfFile = shelve.open('myShelf')
print(list(shelfFile.values())) # [['snatch', 'clean and jerk', 'front squat', 'push press']]
shelfFile.close()