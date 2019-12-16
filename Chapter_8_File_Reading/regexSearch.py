#! python3
#regexSearch.py - Opens all .txt files in a folder and searches for any line that matches
# a user supplied regex expression. Prints the results

import os, re

def search(regex, txt):
    searchRegex = re.compile(regex, re.I)
    result = searchRegex.search(txt)
    print(result)

while True:
    dirs = input("Enter the absolute path of the folder\n")
    if os.path.exists(dirs) == True:
        print("The folder exists")
        break

print("Enter the regular expression:\n")
regex = input()

folder = os.listdir(dirs)

for file in folder:
    if file.endswith(".txt"):
        fileName = os.path.join(dirs, file)
        print(fileName)
        txtFile = open(fileName)
        text = txtFile.read()
        search(regex, text)