from random import randint

def status(chosen_word, guesses):
    stat=''
    for letter in chosen_word:
        if letter in guesses:
            stat += letter
        else:
            stat += '_ '
    print(stat)
    return stat

def new_game(words, played_words, win):
    if (len(played_words)==len(words)):
            print('Thanks for playing!')
            score(win) 
            return False
    else:
        answer = ''
        while (answer!='n' and answer!='y'):
            answer = input('Would you like to play again? ').lower()
            if (answer=='n'):
                score(win)
                return False
            elif (answer=='y'):
                print('Next round!')
                return True
https://github.com/elenasa42/simpleHangman.git            else:
                print('Please enter either "y" or "n" ')

def score(win):
    sc = win*10
    if (sc>=20 and sc<=30):
        print('There is always room for improvement..')
    elif (sc>=40 and sc<=50):
        print('You are halfway hanged.')
    elif (sc>50 and sc<=60):
        print('Not so bad.')
    elif (sc>=70 and sc<=80):
        print('Very nice!')
    elif (sc>=90):
        print('You are the master of the hangman game!')
        
    

words = ['exhibition','reaction','awkward','rogue','yacht',
         'subway','structure','strength','pneumonia','blizzard']
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
_/ \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
_/ \_ |
      |
=========''','''
  +---+  
  |   |
  O   |
 /|\  |
_/ \_ |
      |
=========
  ####
  fire
''']

welcome=['Welcome to hangman! The game is pretty simple,',
         'You will need to guess the word given to you in',
         '9 tries. Let\'s begin!']
for line in welcome:
        print(line)
name = input('What\'s your name? ')
valid_letter='abcdefghijklmnopqrstuvwxyz'
played_words = []
win = 0
play_again = True
remain = len(words)!=len(played_words)
while (play_again and remain):
    attempts = 0
    chosen = randint(0,len(words)-1)
    chosen_word = words[chosen]
    while (chosen_word in played_words):
        chosen = randint(0,len(words)-1)
        chosen_word = words[chosen]
    played_words.append(chosen_word)
    guesses = []
    print(HANGMAN[0])
    guessed=''
    guessed = status(chosen_word, guesses)
    print(name+', the word you have to guess contains '+str(len(chosen_word))+' letters')
    while (attempts<9 and guessed!=chosen_word):
        guess = input('Guess a letter: ').lower()
        if (len(guess)!=1):
            print('You have to enter only one letter!')
        elif (guess not in valid_letter):
            print('That\'s not a letter!')
        elif (guess not in chosen_word):
            if (guess in guesses):
                print('You\'ve already guessed this letter')
            else:
                print('Unfortunately the word does not contain this letter '+guess)
                attempts = attempts + 1
                guesses.append(guess)
                print(HANGMAN[attempts])
                guessed = status(chosen_word, guesses)
        elif (guess in chosen_word):
            if (guess in guesses):
                print('You\'ve already guessed this letter')
            else:
                guesses.append(guess)
                print('The word contains '+guess)
                guessed = status(chosen_word, guesses)
    
        
                
    if (attempts==9):
        print('I\'m sorry '+name+', you lost..')
        print('The word you were looking for was '+chosen_word)
        play_again = new_game(words, played_words,win)

    elif (guessed==chosen_word):
        win += 1
        print('Congradts '+name+', you won!')
        play_again = new_game(words, played_words,win)

