import random
#Menu
def menu():
    print("*********************************")
    print("***Welcome to the Hangman Game***")
    print("*********************************")
    start = input('Do you wanna play? (y or n)').lower()
    if start == 'y':
        selected_word = words()
        letters = split_word(selected_word)
        game(selected_word, letters)
    elif start == 'n':
        print('Ok, bye!')
    else:
        print('Invalid input. Please enter y or n.')
        menu()
#Loading word
def words(): 
    words = ['write', 'book', 'farm', 'computer', 'food', 'guitar', 'police', 'movie', 'letters', 'country']
    random_word = random.choice(words)
    return random_word
#Split selected word
def split_word(random_word):
    letters = [letters for letters in random_word]
    return letters
#Game    
def game(random_word, letters):
    display = '_' * len(random_word)
    print(display)

    #Logic
    guessed_letters = set()
    attempts = 6

    while attempts >= 1:
        guess = input('Guess a letter: ').lower()
        if guess in guessed_letters:
            print('You already guessed that letter. Try again.')
        elif guess in letters:
            guessed_letters.add(guess)
            display = update_display(random_word, guessed_letters)
            print(display)
            if '_' not in display:
                print('Congratulations! You guessed the word:', random_word)
                break
        else:
            attempts -= 1
            print(f'Incorrect guess! {attempts} attempts remaining. The word was {random_word}')

            if attempts == 0:
                print('Sorry, you ran out of attempts. The word was:', random_word)
                break

def update_display(random_word, guessed_letters):
    display = ''
    for letter in random_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

menu()
