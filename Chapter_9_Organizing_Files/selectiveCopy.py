#! python3
# selectiveCopy.py - Walks through a folder tree, then searches and copies for files with a particular extension (i.e. .jpg)

import shutil, os

folder = input('Enter the absolute filepath of'
               ' the directory you wish to copy from: ')

extension = input("Enter the extension you'd like to copy: ")

destination = input("Enter destination folder's absolute filepath: ")

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith(extension):
            shutil.copy(os.path.join(foldername, filename), destination)

print("Selective copy of %s extension from %s to %s is complete" %(extension, folder, destination))