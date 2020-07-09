#! python3

import os

# os.walk returns an iterable with 3 parts, current folder, it's subfolders and it's files.
for folderName, subFolders, filenames in os.walk('.\\dest'):
    print(folderName)
    print(subFolders)
    print(filenames)
    print()