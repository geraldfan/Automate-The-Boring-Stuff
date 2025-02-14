#! python3
# backupToZip.py - Backup folder to zip files, ZIP file's filename increments everytime it is made

import os, zipfile

# Backup the entire contents of "folder" into a ZIP file
def backupToZip(folder):
    folder = os.path.abspath(folder)    #Makes sure folder is absolute
    
    #Figure out the filename this code should use based on the existing files

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number += 1
    
    # Create the ZIP file
    print("Creating %s..." % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, "w")

    # Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print("Adding files in %s..." % (foldername))
        #Add current folder to the ZIP file
        backupZip.write(foldername)
        #Add all the files in this fodler to the ZIP file
        for filename in filenames:
            newBase = os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue
            backupZip.write(os.path.join(foldername,filename))
           
    backupZip.close()
    print("Done")

backupToZip("C:\\Users\\Gerald\\Desktop\\code")
