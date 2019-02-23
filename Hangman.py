'''
Created on Oct 27, 2018

@author: ITAUser
'''
import random

#picks random words 
def pick_random_word():
    #opens the woed dictionary
    with open("words.txt",'r') as f:
        words = f.readlines()
    
    #generates a random index
    # -1 b/c len(words) is not a valid index into the list 'word'
    index = random.randint(0, len(words) -1)
    
    #prints out the word at the index
    word = words[index].strip()
    return word

#takes an input from the user and returns the letter that was guessed
def ask_user_for_next_letter():
    letter = input("guess your letter: ")
    return letter.strip().upper()
    #strip removes all spaces
    
#creates string that has letters guessed correctly and _ for letters not guessed 
def generate_word_string(word, letters_guessed):
    output = []
    
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
            #append adds an index to a string or list
        else:
            output.append("_")
    return " ".join(output)
    
#main body of the program - looked through first 
if __name__ == '__main__':
    WORD = pick_random_word()
    letters_to_guess = set(WORD)
    
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()
    num_guesses = 0 
    
    #user prompt 
    print("welcome to hangman!")
    
    while (len(letters_to_guess) > 0)  and num_guesses < 6 :
        guess = ask_user_for_next_letter()
        guess = guess.lower()
        
        #check if we already guessed the letter
        if guess in correct_letters_guessed or guess in incorrect_letters_guessed:
            print("you already guessed that letter.")
            continue 
        
        #check if letter guessed is in the word 
        if guess in letters_to_guess:
            letters_to_guess.remove(guess)
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            #updates the number of guessed left adds 1 when guessed incorrectly
            num_guesses += 1
            
        word_string = generate_word_string(WORD, correct_letters_guessed)
        print(word_string)
        print("you have  " + str(6 - num_guesses) + " guesses left.")
        
    #tells the user if they won or not
    if num_guesses < 6:
        print("congratuations! you correctly guessed the word " + WORD)
    else:
        print("sorry, you lost! your word was " + WORD)
            