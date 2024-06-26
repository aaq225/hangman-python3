import random

from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)

guess_list = []
live_count = 6
for letter in chosen_word:
    guess_list.append("_")
user_won = False
while not user_won:
    user_letter = input("Guess a letter: ").lower()
    
    if user_letter in guess_list:
        print(f"You've already guessed {user_letter}")
        
    
    for i in range(0, len(chosen_word)):
        if chosen_word[i] == user_letter:
            guess_list[i] = user_letter
            
    print(f"{' '.join(guess_list)}")

    if user_letter not in chosen_word:
        print(f"You guessed {user_letter}, that's not in the word. You lose a life.")
        live_count -= 1
        print(f"Current live count: {live_count}")
    print(stages[live_count])
          
    if live_count == 0:
        print(f"Game Over!\n The word was {chosen_word}.")
        break        
            
    
    if ''.join(guess_list) == chosen_word:
        user_won = True
        print("You won!")
        break
    
    
    

   