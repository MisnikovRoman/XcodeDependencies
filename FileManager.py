import os
import json

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

def readToLinesFile(path):
    file = open(path, 'r')
    lines = file.readlines()
    file.close()
    return lines


def dictFromJson(path):
    #  Открытие файла с уверенностью, что он будет закрыт
    with open(path, 'rb') as file:
        dict = json.load(file)
        return dict

