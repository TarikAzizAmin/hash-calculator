#!/usr/bin/env/python3

import hashlib

BUFF_SIZE = 65536
sha256 = hashlib.sha256()


def checkFileIntegrity(calculatedHash, originalHash):
    return calculatedHash == originalHash


def calHash(file):
    with open(file, 'rb') as file:

        while True:
            data = file.read(BUFF_SIZE)

            if not data:
                break
            sha256.update(data)
    calculatedHash = sha256.hexdigest()
    check = checkFileIntegrity(calculatedHash, originalHash)
    if check == False:
        print(f"File {fileLocation} 's integrity has been compromised, should not trues this file")
    elif check == True:
        print(f"{fileLocation} is secure and verified")


if __name__ == "__main__":
    fileLocation = input("Please enter the file location:\n")
    originalHash = input("please enter the expected hash for this file\n")

    try:
        calHash(fileLocation)
    except Exception as e:
        print(f"An error occurred {str(e)}")