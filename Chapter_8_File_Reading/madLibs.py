#! python3
# madLibs.py - Takes in a text file and lets the user their own
# words anywhere the word ADJECTIVE,NOUN, ADVERB, or VERB appears in the text file

import re

textFile = open(
    "C:\\Users\\Gerald\\Desktop\\Python\\Chapter_8_File_Reading\\madlibs.txt")
textContent = textFile.read()
textFile.close()

check = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")

while True:
    result = check.search(textContent)

    if result == None:
        break

    if result.group() == "ADJECTIVE" or result.group() == "ADVERB":
        print("Please enter an %s" % result.group().lower())
    else:
        print("Plase enter a %s" % result.group().lower())
    word = input()

    textContent = check.sub(word, textContent, 1)
    print(textContent)

print("Name the file")
name = input()
newFile = open(
    "C:\\Users\\Gerald\\Desktop\\Python\\Chapter_8_File_Reading\\%s.txt" % (name), "w")
newFile.write(textContent)
