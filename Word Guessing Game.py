#imports
import random

#Playing Game
wins = 0
losses = 0
play_again = 'y'
while play_again == 'y':
#Word Dictionary
    words_used = []
    word_list = open("words_alpha.txt")
    words = word_list.readlines()
    word=words[random.randint(0,len(words)-1)]
    reuse = False
    for a in words_used:
        if word is a:
            reuse = True
            break
    if reuse:
        continue

    print("Welcome to my game. You currently have " + str(wins) + " wins and " + str(losses) + " losses. Good luck :)")
    list_word = list(word)
    length = len(word)
    guess_remaining = 7
    already_guessed = set()

#Guessing letter/word
    guess = ' '
    while guess != word and guess_remaining > 0:
        dash = ""
        for i in range(0, len(word)-1):
            if word[i] in already_guessed:
                dash += word[i] + ""
            else:
                dash+="_"
        list_dash = list(dash)
        print(list_dash)
        print('The word contains ' + str(len(word)-1) + " letters.")        
        guess_type = str(input('Are you guessing a word or a letter? '))
        if guess_type != 'word' and guess_type != 'letter':
            print ('Please enter "word" or "letter".')
        elif guess_type == 'word':
            guess = str(input('What word are you guessing? '))
            if guess in already_guessed:
                print ('You have already guessed that word. Guess again')
            else:
                guess_remaining = guess_remaining - 1
                already_guessed.add(guess)
        else:
            guess = str(input('What letter are you guessing? '))
            if len(guess) < 1 or len(guess) > 1:
                print('Please enter a single letter')
            if guess in already_guessed:
                print("You have already guessed that letter. Guess again")
            else:
                already_guessed.add(guess)
                if guess in word:
                    print("Congrats, you found a letter")
                else:
                    print("That letter is not in the word")
                    guess_remaining = guess_remaining - 1 
        if guess_remaining == 7:
            print("_____")
            print("  ")
            print("  ")
            print(" ")
            print("")            
        if guess_remaining == 6:
            print("_____")
            print("  | ")
            print("  ")
            print(" ")
            print("") 
        if guess_remaining == 5:
            print("_____")
            print("  | ")
            print("  O ")
            print(" ")
            print("") 
        if guess_remaining ==4:
            print("_____")
            print("  | ")
            print("  O ")
            print("  | ")
            print("")
        if guess_remaining == 3:
            print("_____")
            print("  | ")
            print("  O ")
            print("  | ")
            print(" /  ")
        if guess_remaining == 2:
            print("_____")
            print("  | ")
            print("  O ")
            print("  | ")
            print(" / \ ")
        if guess_remaining == 1:
            print("_____")
            print("  | ")
            print("  O ")
            print(" /| ")
            print(" / \ ")
        if guess_remaining == 0:
            print("_____")
            print("  | ")
            print("  O ")
            print(" /|\ ")
            print(" / \ ")          
        print("You have " + str(guess_remaining) + " guesses remaining")
    if guess == word:
        print("Congrats, you guessed the word")
        wins = wins +1
    else:
        print("You did not guess the word and are out of guesses")
        print("The word was " + word)
        losses = losses + 1

    play_again = str(input("Would you like to play again (y/n) "))
