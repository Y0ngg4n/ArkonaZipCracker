import rarfile, zipfile
import exrex
from pathlib import Path

def askMode():
    return input(
        "Enter (1) to generate a Password List, (2) to use an existing Password List or (3) to BruteForce without Password List. Please enter: (1/2/3) ")


def getPasswordListFromExpression():
    expression = input("Regex Expression for Password Definition: ")
    print("Generating Password-List...")
    return list(exrex.generate(expression))

def writePasswordList(passwordList):
    print("Writing Password-List to File...")
    with open('passwordList.txt', 'w') as passwordListFile:
        for item in passwordList:
            passwordListFile.write("%s\n" % item)
    print("Finished writing Password-List to File...")

def dictionaryAttack(passwordList, offset):
    password = None
    with open(passwordList, 'r') as passwordList:
        lines = passwordList.readlines()
        fileName = getFile();
        if getFileExtension(fileName) == ".zip":
            zipFile = zipfile.ZipFile(fileName)
            for i in range(offset, len(lines)):
                password = lines[i].strip('\n')
                try:
                    print("Trying password: " + password + " | Offset: " + str(i))
                    zipFile.extractall(pwd=password)
                    print("\nPassword found: " + password)
                    return
                except:
                    print("Trying next password...")
                    pass
        elif getFileExtension(fileName) == ".rar":
            rarFile = rarfile.RarFile(fileName)
            for i in range(offset, len(lines)):
                password = lines[i].strip('\n')
                try:
                    print("Trying password: " + password + " | Offset: " + i)
                    rarfile.extractall(pwd=password.encode())
                    print("\nPassword found: " + password)
                    return
                except:
                    print("Trying next password...")
                    pass
def bruteforce():
    fileName = getFile();
    if getFileExtension(fileName) == ".zip":
        zipFile = zipfile.ZipFile(fileName)
        passwordList = getPasswordListFromExpression()
        for password in passwordList:
            password = password.strip('\n')
            try:
                print("Trying password: %s" % password)
                zipFile.extractall(pwd=password.encode())
                print("\nPassword found: " + password)
                return
            except:
                print("Trying next password...")
                pass
    elif getFileExtension(fileName) == ".rar":
        rarFile = rarfile.RarFile(fileName)
        passwordList = getPasswordListFromExpression()
        for password in passwordList:
            password = password.strip('\n')
            try:
                print("Trying password: %s" % password)
                rarfile.extractall(pwd=password.encode())
                print("\nPassword found: " + password)
                return
            except:
                print("Trying next password...")
                pass

def getFile():
    return input("Archive Filename: ")

def getFileExtension(name):
    return Path(name).suffix

def main():
    mode = askMode()
    if mode == "1":
        print("*** Password-List Generation ***")
        writePasswordList(getPasswordListFromExpression())
    elif mode == "2":
        print("*** Dictionary Attack **")
        passwordList = input("Please enter Path to Password-List: ")
        offset = input("Please enter Password-List offset: ")
        dictionaryAttack(passwordList, int(offset))
    elif mode == "3":
        print("*** BruteForce Attack **")
        bruteforce()
    else:
        print("Please enter a valid Mode next time...")

if __name__ == "__main__": main()
