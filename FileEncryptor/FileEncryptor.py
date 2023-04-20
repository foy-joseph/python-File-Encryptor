import random, datetime, re

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def getWordListFromFile(fileName):
    try:
        openedFile = open(fileName, "r")
        readFile=openedFile.read()
        wordsList = re.split("\n|-| ",readFile) # covert to list divided by "\n", "-", " "
        wordsListFinal = []
        for word in wordsList:
            word.removesuffix(".")
            word.removesuffix(",")
            if word.isalpha():
                wordsListFinal.append(word)
    except:
        print("Error: invalid file type")
    finally:
        openedFile.close()
    try:
        return wordsListFinal
    except: 
        return None

def selectRandomKey(listIn):
    eightLetterList = []
    for word in listIn:
        word=str(word)
        if len(word)>7:
            eightLetterList.append(word) # gather all eight letter and more words
    try:
        randInt = random.randint(0, len(eightLetterList)) # get random index of the list
        return eightLetterList[randInt] 
    except:
        print("Error: list index invalid. try again")
       

def callOption1Or2(): # Display contents of any csv or txt file on screen
    fileName = input("Enter relative path of file: ")
    try:
        openFile = open(fileName, "r")
        print(openFile.read())
    except:
        print("Error: Incorrect directory or file given. try again")
    finally:
        openFile.close()

def callOption3(): # Select a key word
    fileName = input("Enter relative path of file from which key will be selected: ")
    try:
        words = getWordListFromFile(fileName)
        key = selectRandomKey(words)
        key = str(key).strip()
        keyFile = open("CA2\Files\keys.txt", "a")
        keyFile.write(key)
        keyFile.write("---")
        keyFile.write(str(datetime.datetime.now())) # time stamp
        keyFile.write("\n")
        print(key)
        print("your random key is [",key,"]")
    except:
        print("Error: Incorrect directory or file given. try again")
    finally:
        keyFile.close()

def callOption4(): # Generate an encryption string
    try:
        word = list(input("Enter key word: ").lower())
    except:
        print("all characters in keyword must be alphabetic! try again")
        return None
    try:
        alphaRev = alpha[::-1]
        word.reverse() # last duplicate of letter in word has to be removed - reverse it
        for letter in word:
            if word.count(letter)>1:
                word.remove(letter)
        word.reverse() # reverse word again to put it into proper order
        for letter in alphaRev:
            if letter in word:
                alphaRev.remove(letter)
        alphaEnc=str()
        for letter in word:
            alphaEnc+=letter
        for letter in alphaRev:
            alphaEnc+=letter
        print("Your Encryption string is [",alphaEnc,"]")
    except:
        print("error in encryption string generation. Please try again.")
        return None

def callOption5(): # encrypt a file
        fileName=input("Enter the file relative path: ")
        encString = callOption4()
        if fileName.endswith("Enc.txt") or fileName.endswith("V1.txt"): # dont interact with files that have already been interacted with
            print("File already encrypted / decrypted! ")
        else:
            newFileName = fileName.replace(".txt", "Enc.txt")
            try:
                openedFile = open(fileName, "r")
                readFile = openedFile.read()
                newFile =  open(newFileName, "w")
                for char in readFile:
                    char=str(char).lower()
                    if char.isalpha() and char in readFile: # convert the origional letter to new letter
                        alpIndex = alpha.index(char)
                        newFile.write(encString[alpIndex])
                    else:
                        newFile.write(char) # all non alphabetical characters will still be written
            except:
                print("error in encoding file. ")
            finally:
                newFile.close()
                openedFile.close()

def callOption6():# decrypt a file 

    fileName=input("Enter the file relative path: ")
    encString = callOption4()

    if fileName.endswith("Enc.txt"):
        newFileName = fileName.replace("Enc.txt", "V1.txt")
        try:
            openedFile = open(fileName, "r")
            readFile = openedFile.read()
            newFile =  open(newFileName, "w")
            for char in readFile:
                char=str(char).lower()
                if char.isalpha() and char in readFile:
                    alpIndex = encString.index(char) # - process is identical to option 5 except for here- reverse order
                    newFile.write(alpha[alpIndex])
                elif not char.isalpha():
                    newFile.write(char)
        except:
            print("invalid fileName. try again")

        finally:
            newFile.close()
            openedFile.close()
    else:
        print("invalid fileName. try again")

def main():
    while(True):
        print("\n")
        print("1. Display contents of any csv file on screen")
        print("2. Display contents of any text file on screen")
        print("3. Select a key word")
        print("4. Generate an encryption string")
        print("5. Encrypt a file")
        print("6. Decrypt a file")
        print("7. Quit")
        try:
            option = int(input("Choose 1-7: "))
            if option == 1 or option == 2:
                callOption1Or2()
            elif option == 3:
                callOption3()
            elif option == 4:
                callOption4()
            elif option == 5:
                callOption5()
            elif option == 6:
                callOption6()
            elif option == 7:
                break
            else:
                print("Invalid number! Enter single character numbers from 1-7")
        except:
            print("Invalid input! Enter single character numbers from 1-7")

#testing
#callOption2() works
#callOption1() works
#callOption3() works
#callOption4() works
#callOption5() works
#callOption6() works
main()