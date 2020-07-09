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
