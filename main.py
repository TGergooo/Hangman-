
from replit import clear
import random
from hangman_words_hun import hangman_words_hun
from hangman_words import word_list
from hangman_art import stages,logo,trophy
from retry import eng_or_hun,eng_retry,hun_retry

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
gamer=0
computer=0
end_of_game = False
lives = 6
chosed="You typed that letters--> "
print(logo)

languag=input(f"Press 'H' to Hungary or type 'E' to English language!\n")
language=languag.capitalize() 


if language == 'E':
  display = []
  dash="-"
  for _ in range(word_length):
    display += "_"
  for position in range(word_length):
      if chosen_word[position] == '-':
          display[position] = '-'
  while not end_of_game:
      guess = input("Guess a letter: ").lower()
      clear()
  
      if guess in display:
        print(f"You've already guessed {guess}.")
      
          
      for position in range(word_length):
          letter = chosen_word[position]
          # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter
  
      if guess not in chosen_word:
          lives -= 1
          print(f"You guessed {guess} that's not in the word.You lose a life.")
          if lives == 0:
              end_of_game = True
              print(f"You lose.The right word is {chosen_word}")
              print("A new game begins!")
              eng_retry()
            
      print(f"{' '.join(display)}")
  
      if "_" not in display:
          end_of_game = True
          print("               You win!")
          print(trophy)
      if guess not in chosen_word:
        chosed+=guess+"..."
      print(stages[lives])
      print(chosed)

if language == 'H':
  hun_retry()
else:
  print("Please type a correct letter!Try agin!(Rossz betűt írtál be, próbáld újra!)")
  eng_or_hun()