#! python3

# Reading from a file
helloFile = open('.\\hello.txt')
content = helloFile.read() # returns the entire contents as a string
helloFile.close()
print(content) #Hello World!\nHow are you?

helloFile = open('.\\hello.txt')
content = helloFile.readlines() # returns a list of strings, each line a separate string
helloFile.close()
print(content) # ['Hello World!\n', 'How are you?']

# Writing to a file
helloFile = open('.\\hello.txt', 'w') # w for write mode, rewrites the entire file
helloFile.write('I am well thank you.\nHow are things?')
helloFile.close()

# Read it back and print...
helloFile = open('.\\hello.txt')
content = helloFile.read()
helloFile.close()
print(content) # I am well thank you.\nHow are things?

# Appending to a file
helloFile = open('.\\hello.txt', 'a') # a for append mode, adds new text to the end of the file.
helloFile.write('\nPretty good thanks for asking!')
helloFile.close()

# Read it back and print...
helloFile = open('.\\hello.txt')
content = helloFile.read()
helloFile.close()
print(content) # I am well thank you.\nHow are things?\nPretty good thanks for asking!

# Creating a file
# Using a or w, if the file doesn't exist, it will be created.
goodbyeFile = open('.\\goodbye.txt', 'w')
goodbyeFile.write('Nice chatting with you, goodbye!')
goodbyeFile.close()

goodbyeFile = open('.\\goodbye.txt') # mode is r for read by default
content = goodbyeFile.read()
print(content) # Nice chatting with you, goodbye!