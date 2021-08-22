
#rewrite the whole thing using classes?
#what if we wanted to add possibility to get a hint
#change the logic for possibility to guess the word. it should not appear at the first letter you guess
#make list for words longer & remove 3 letters strings?
#keep the guessed letters even if they are wrong, so they don't count as a guess?

from list_of_words import words
from random import choice
import re
import sys


letter_guessed=[]

def start():
    chosen_word = choice(words)
    length = len(chosen_word)
    number_guess= length + 2
    guesses=0
    print('Welcome to the Hangman game vers. 666')
    print('The word you have to guess is ', len(chosen_word), ' letters long')
    print(''.join('_' for letter in chosen_word))
    print ('You have only ', number_guess, ' guesses, so be careful!')
    guess_letters(guesses, chosen_word, number_guess)
       
    
#the following should be simplified
def guess_letters(guesses, chosen_word, number_guess):
    
    if guesses != number_guess:
            letter=input('Guess a letter: ').lower()
            if len(letter) != 1:
                print ("Error! You can only guess 1 letter!")
                guess_letters(guesses, chosen_word, number_guess)
            elif not re.match("^[a-z]*$", letter):
                print ("Error! Only letters are allowed!") #this only works if single number is the input
                guess_letters(guesses, chosen_word, number_guess)
            else:
                guesses +=1
                if letter in chosen_word and letter not in letter_guessed:
                    print('Nice! That is correct:')
                    letter_guessed.append(letter)
                    hidden_word= (''.join( c if c in letter_guessed else '_' for c in chosen_word))
                    if hidden_word != chosen_word:
                        print(hidden_word)
                        print()
                        print('Number of guesses: ',guesses)
                        guess_word(guesses, chosen_word, number_guess)

                    elif hidden_word==chosen_word:
                        print('You found the word!')
                        print(hidden_word)
                        restart()
                        
                    
                elif letter in letter_guessed:
                    print('You have already found this letter.')
                    print('Number of guesses: ',guesses)
                    guess_letters(guesses, chosen_word, number_guess)
                           
                else:
                    print ('Nope. Try again.')
                    hidden_word= (''.join( c if c in letter_guessed else '_' for c in chosen_word))
                    print()
                    print('Number of guesses: ',guesses)
                    print(hidden_word)
                    guess_letters(guesses, chosen_word, number_guess)
    if guesses == number_guess:
        print('That was the last guess! Try to guess the word.')
        win(chosen_word)     
        
def guess_word(guesses, chosen_word, number_guess):

    try_guess = input('Would you like to guess the word? Type Yes to guess the word or No to continue guessing letters. ').lower()
    if try_guess == 'yes':    
        win(chosen_word)
    elif try_guess == 'no':
        guess_letters(guesses, chosen_word, number_guess)        
    else:
        print('Ups! You missed the opportunity to guess the word. Try again... That was not quite clear')
        guess_letters(guesses, chosen_word, number_guess)  

def win(chosen_word):
        the_word=input('And the word is....? ')
        if the_word == chosen_word:
            print('Amazing! You win!')
            
        else:
            print('You lost! :(')
            print('The word was ', chosen_word)
           
        restart()

        
def restart():
    again = input('Would you like to start again? Type Yes to restart or No to exit. ').lower()
    if again == 'yes':
        letter_guessed.clear()
        start()
    elif again == 'no':
        print('This was fun! Have a good one until next time!')
        sys.exit()
        #find another way to exit the system 
    else:
        print('What did you say? Try once more.')
        restart()                       
    
start()

# a little thing
