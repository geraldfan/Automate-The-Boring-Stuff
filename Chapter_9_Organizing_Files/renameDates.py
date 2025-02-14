# 1 python3
# renameDates.py - Renames filenames with American dates mm-dd-yyyy to
# European dates dd-mm-yyyy

import shutil
import os
import re

# Create a regex that matches the mm-dd-yyyy American date format

datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-         #one or two digits for the month
    ((0|1|2|3)?\d)-     #one or two digits for the day
    ((19|20)\d\d)       #four digits for the year
    (.*?)$              #all text after the date
""", re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir("."):
    mo = datePattern.search(amerFilename)

    #Skip files without a date
    if mo == None:
        continue

    #Getting the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# Form the European-style filename.
    euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart

# Get the full, absolute file paths.
    absWorkingDir = os.path.abspath(".")
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

# Rename the files.
    print("Renaming %s to %s..." % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)