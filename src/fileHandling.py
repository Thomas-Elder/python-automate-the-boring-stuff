#! python3

import shutil

# Copy takes source file and destination folder and copies the file there
# It returns a string of the new file
print(shutil.copy('.\\hello.txt', '.\\dest')) # .\dest\hello.txt

# Can rename the file as well, by specifying the name in the destination string
print(shutil.copy('.\\hello.txt', '.\\dest\\hellothere.txt')) # .\dest\hellothere.txt

# Can copy a whole folder with
print(shutil.copytree('.\\', '.\\dest\\backup'))