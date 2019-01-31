import json
import os
from random import randint

directory = './Category/'
file_location = './Category/'
file_list = []
category_list = []
user_category = ''
word_list = {}
loaded_JSON = {}


def listword_list():
    global category_list
    print('Category:')
    file_list = os.listdir(directory)
    num = 1
    for i in file_list:
        name = i.split('.')[0]
        if name:
            print(num, end='.')
            print(name)
            num += 1
            category_list.append(name)


def chooseword_list():
    global user_category
    user_input = int(input('Choose Your Category Number: '))

    while user_input > len(category_list):
        user_input = int(input('Choose New Category Number: '))

    print('Category: ', end='')
    print(category_list[user_input-1])
    user_category = category_list[user_input-1]


def show_hint(num):
    print('Hint: \" ', end='')
    for i in loaded_JSON['HINT'].split(' '):
        if i[0] == '$':
            print(word_list[num][i[1:]], end=' ')
        else:
            print(i, end=' ')
    print('\"')


def rand():
    global file_location, word_list, loaded_JSON
    file_location = file_location + user_category+'.json'
    print(file_location)
    f = open(file_location, 'r')
    loaded_JSON = json.load(f)
    word_list = loaded_JSON['WORDLIST']
    random_number = randint(1, len(word_list))
    random_number -= 1
    return random_number


def hangman(word):
    tmp_blind = ''
    blind = []
    score = 0
    ramain_wrong_guess = 10
    length_char_to_answer = 0
    wrong_guess = []
    for char in word:
        if char.isalpha():
            tmp_blind = tmp_blind+'_'
            length_char_to_answer += 1
        else:
            tmp_blind = tmp_blind+char
    blind = list(tmp_blind)
    while length_char_to_answer != 0 and ramain_wrong_guess != 0:
        for i in blind:
            print(i, end=' ')

        print('Score ', end='')
        print(score, end=' ')

        print('Remaining wrong guess ', end='')
        print(ramain_wrong_guess, end=' ')

        print('Wrong guess ', end='')
        print(wrong_guess)

        guess = input('> ')
        if len(guess) > 1:
            continue
        guess = guess.lower()
        correct = False
        for i in range(0, len(blind)):
            if blind[i] == '_' and word[i].lower() == guess:
                score += 5
                blind[i] = word[i]
                length_char_to_answer -= 1
                correct = True
        if not correct and guess not in wrong_guess and guess not in word and guess.isalpha():
            ramain_wrong_guess -= 1
            wrong_guess.append(guess)

    if length_char_to_answer == 0:
        print('Congratulation! you won with word ' +
              word + ' and score '+str(score)+' Pts.')
    else:
        print('You Lose! so the word is '+word +
              ' and score '+str(score)+' Pts.')


if __name__ == "__main__":
    listword_list()
    chooseword_list()
    random_number = rand()
    show_hint(random_number)
    word = word_list[random_number]['TITLE']
    hangman(word)
