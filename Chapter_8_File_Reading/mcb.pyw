#! python3
# mcb.pyw - Saves and loads pieces of text to the clibboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#   py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#   pw.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print("1")
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1] == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
        print("2")
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(mcbShelf[sys.argv[1]])
mcbShelf.close()