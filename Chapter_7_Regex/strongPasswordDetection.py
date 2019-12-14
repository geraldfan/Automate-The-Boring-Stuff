#! python3
# strongPasswordDetection.py Checks if the password detected is strong

import re

def isStrongPassword(pw):
    capRegex = re.compile(r'[A-Z]')
    lowRegex = re.compile(r'[a-z]')
    digitRegex = re.compile(r'[0-9]')

    if capRegex.search(pw) and lowRegex.search(pw) and digitRegex.search(pw) and len(pw) > 7:
        return True
    return False

print("Enter a password: ")
print(isStrongPassword(input()))