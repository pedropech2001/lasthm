import random

WORDLIST_FILENAME = "pedro.txt"

def loadfile():
#load file data
    inFile = open(WORDLIST_FILENAME, 'r')
    #read every word in the file
    line = inFile.readline()
    wordlist = line.split()
    #Print the number of possible words in the file, 14
    print("  ", len(wordlist), "words in the file")
    return wordlist

def chooseWord(wordlist):
  #choose a random word in the file
    return random.choice(wordlist)

wordlist = loadfile()

def isWordGuessed(secretWord, lettersGuessed):
    # find if we guess a letter of the secret word
    #and and if its true or false
    for c in secretWord:
        if c not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
#prints the letter we already guess if not print _
    cword=''
    for c in secretWord:
        if c in lettersGuessed:
            cword+=c
        else:
            cword+=' _'
    return cword


def getAvailableLetters(lettersGuessed):
    import string
    #shows the available letters in the abc
    abc=string.ascii_lowercase
    letters=''
    for c in abc:
        if c not in lettersGuessed:
            letters+=c
    return letters
    

def hangman(secretWord):

    print('This is the Pedro´s Hangman game!')
    print('The first hint is that your word is', len(secretWord), ' letters long.')
    print(" ")

#lives
    guessesAvailable=10
    lettersGuessed=''
    

    while not isWordGuessed(secretWord,lettersGuessed):
# shows your lives
        print('You have', guessesAvailable, 'lives left.')
        #show the letters we can use from abc
        print('Available letters:', getAvailableLetters(lettersGuessed))
        #print the option to guess a letter in the word
        guess=input('Please guess a letter:')
        guesslc=guess.lower()
        #this are the cases that can be in the game
        #if you repeat a letter
        if guesslc in lettersGuessed:
            print("hey you already put that letter:", getGuessedWord(secretWord,lettersGuessed))
        #if your letter is correct
        elif guesslc in secretWord:
            lettersGuessed+=guesslc
            print('Your letter is correct:', getGuessedWord(secretWord,lettersGuessed))
        #if your letter is incorrect
        else:
            print('Hey that letter is not in the word:', getGuessedWord(secretWord,lettersGuessed))
            lettersGuessed+=guesslc
            guessesAvailable-=1

        print("")
        if guessesAvailable==0:
            print('Sorry you died', secretWord , '.')
            return False
        

    print ("Hey you won!")
    return True

#Game launch and uses a random word in the file
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
