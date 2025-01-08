from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess(guess):


    while guess not in ['0','1','2']:
        guess = input('choose a number:0,1 or 2')

    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'o':
        print('correct answer')
    else:
        print('wrong answer')
        print(mylist)

mylist = [' ','o',' ']

guess = ''

setup_list = shuffle_list(mylist)

choice = player_guess(guess)

check_guess(setup_list,choice)