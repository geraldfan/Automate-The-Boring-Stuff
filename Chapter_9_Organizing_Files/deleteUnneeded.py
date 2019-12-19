#! python3
# deleteUnneeded.py - Walks through folder tree and prints large files or folders

import os

folder = input("Enter the folder you wish to analyze:")
size = int(input("Enter the size in MB:")) * 10**6

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        filesize = os.path.getsize(os.path.join(foldername, filename))
        if filesize > size:
            print(os.path.join(foldername, filename) + " " +
                  str(filesize / (10**6)) + " MB")
