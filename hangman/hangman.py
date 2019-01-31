import json
import os
from random import randint

directory = './wordlist/'
file_location = './wordlist/'
filelist = []
categoryList = []
userCategory = ''
wordlist = {}
loadedJSON = {}


def listWordList():
    global categoryList
    print('Category:')
    filelist = os.listdir(directory)
    num = 1
    for i in filelist:
        name = i.split('.')[0]
        if name:
            print(num, end='.')
            print(name)
            num += 1
            categoryList.append(name)


def chooseWordList():
    global userCategory
    userInput = int(input('Choose Your Category Number: '))

    while userInput > len(categoryList):
        userInput = int(input('Choose New Category Number: '))

    print('Category: ', end='')
    print(categoryList[userInput-1])
    userCategory = categoryList[userInput-1]


def showHint(num):
    print('Hint: \" ', end='')
    for i in loadedJSON['HINT'].split(' '):
        if i[0] == '$':
            print(wordlist[num][i[1:]], end=' ')
        else:
            print(i, end=' ')
    print('\"')


def rand():
    global file_location, wordlist, loadedJSON
    file_location = file_location + userCategory+'.json'
    print(file_location)
    f = open(file_location, 'r')
    loadedJSON = json.load(f)
    wordlist = loadedJSON['WORDLIST']
    randomNumber = randint(1, len(wordlist))
    randomNumber -= 1
    return randomNumber


def hangman(word):
    tmpBlind = ''
    blind = []
    score = 0
    ramainWrongGuess = 10
    lenCharToAns = 0
    wrongGuess = []
    for char in word:
        if char.isalpha():
            tmpBlind = tmpBlind+'_'
            lenCharToAns += 1
        else:
            tmpBlind = tmpBlind+char
    blind = list(tmpBlind)
    while lenCharToAns != 0 and ramainWrongGuess != 0:
        for i in blind:
            print(i, end=' ')

        print('Score ', end='')
        print(score, end=' ')

        print('Remaining wrong guess ', end='')
        print(ramainWrongGuess, end=' ')

        print('Wrong guess ', end='')
        print(wrongGuess)

        guess = input('> ')
        if len(guess) > 1:
            continue
        guess = guess.lower()
        correct = False
        for i in range(0, len(blind)):
            if blind[i] == '_' and word[i].lower() == guess:
                score += 5
                blind[i] = word[i]
                lenCharToAns -= 1
                correct = True
        if (not correct) and (guess not in wrongGuess) and guess not in word:
            ramainWrongGuess -= 1
            wrongGuess.append(guess)

    if lenCharToAns == 0:
        print('Congratulation! you won with word ' +
              word + ' and score '+str(score)+' Pts.')
    else:
        print('You Lose! so the word is '+word +
              ' and score '+str(score)+' Pts.')


if __name__ == "__main__":
    listWordList()
    chooseWordList()
    randomNumber = rand()
    showHint(randomNumber)
    word = wordlist[randomNumber]['TITLE']
    hangman(word)
