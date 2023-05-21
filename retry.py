def eng_or_hun():
  from replit import clear
  import random
  from hangman_words_hun import hangman_words_hun
  from hangman_words import word_list
  from hangman_art import stages,logo,trophy
  from retry import eng_or_hun,eng_retry,hun_retry
  
  chosen_word = random.choice(word_list)
  word_length = len(chosen_word)
  
  end_of_game = False
  lives = 6
  chosed="You typed that letters--> "

  
  languag=input(f"Press 'H' to Hungary or type 'E' to English language!\n")
  language=languag.capitalize() 

  if language == 'E':
    display = []
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
  # hungary chapter start here   
    chosen_wordH = random.choice(hangman_words_hun).lower()
    word_length = len(chosen_wordH)
    
    end_of_game = False
    lives = 6
    chosedH="Ezeket a betűket írtad be eddig--> "  
    display = []
    for _ in range(word_length):
        display += "_"
    for position in range(word_length):
      if chosen_wordH[position] == '-':
        display[position] = '-'
          
    while not end_of_game:
        guess = input("Tippelj egy betűt: ").lower()
        clear()
        
        if guess in display:
          print(f"Már próbáltad ezt a betűt: {guess}.")
          
              
        for position in range(word_length):
            letter = chosen_wordH[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter
      
        if guess not in chosen_wordH:
            lives -= 1
            print(f"Ezt tippelted {guess} ez a betű nincs benne a szóban.Vesztettél egy életet.")
            if lives == 0:
                end_of_game = True
                print(f"Vesztettél.A megfejtés {chosen_wordH}")
                print("Új játék kezdődik!")
                hun_retry()
              
        print(f"{' '.join(display)}")
      
        if "_" not in display:
            end_of_game = True
            print("               Nyertél!")
            print(trophy)
        if guess not in chosen_wordH:
          chosedH+=guess+"..."
        print(stages[lives])
        print(f'Ennyi betűből áll a szó: {word_length}')
        print(chosedH)
  else:
    print("Please type a correct letter!Try agin!(Rossz betűt írtál be próbáld újra!)")

def eng_retry():
  
  from replit import clear
  import random
  from hangman_words_hun import hangman_words_hun
  from hangman_words import word_list
  from hangman_art import stages,logo,trophy
  from retry import eng_or_hun,eng_retry,hun_retry
  
  chosen_word = random.choice(word_list)
  word_length = len(chosen_word)
  
  end_of_game = False
  lives = 6
  chosed="You typed that letters--> "


  

  display = []
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

gamer=0
computer=0
def hun_retry():
    
  from replit import clear
  import random
  from hangman_words_hun import hangman_words_hun
  from hangman_words import word_list
  from hangman_art import stages,logo,trophy
  from retry import eng_or_hun,eng_retry,hun_retry
  
# hungary chapter start here   
  chosen_wordH = random.choice(hangman_words_hun).lower()
  word_length = len(chosen_wordH)
  global gamer
  global computer
  end_of_game = False
  lives = 6
  chosedH="Ezeket a betűket írtad be eddig--> "  
  
  display = []
  for _ in range(word_length):
      display += "_"
  for position in range(word_length):
    if chosen_wordH[position] == '-':
        display[position] = '-'
      
  while not end_of_game:
      guess = input("Tippelj egy betűt: ").lower()
      clear()
    
      if guess in display:
        print(f"Már próbáltad ezt a betűt: {guess}.")
        
            
      for position in range(word_length):
          letter = chosen_wordH[position]
          # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter
    
      if guess not in chosen_wordH:
          lives -= 1
          print(f'Ezt tippelted "{guess}" ez a betű nincs benne a szóban.Vesztettél egy életet.')
          if lives == 0:
              end_of_game = True
              print(f"Vesztettél.A megfejtés {chosen_wordH}")
              computer=computer+1
              print("Új játék kezdődik!")
              hun_retry()
                
                
              
      print(f"{' '.join(display)}")
    
      if "_" not in display:
          end_of_game = True
          print("               Nyertél!")
          gamer=gamer+1
          print(trophy)
          hun_retry()
      if guess not in chosen_wordH:
        chosedH+=guess+"..."
      print(stages[lives])
      print(f'Ennyi betűből áll a szó: {word_length}')
      print(chosedH)
      if computer>gamer:
        print('|>----------------------------------------------------------------------------<|')
        print("|***********************Érzem az erőt , semmi esélyed!*************************|")
      if computer==gamer:
        print('|>----------------------------------------------------------------------------<|')
        print("|¤¤¤¤¤¤¤Nem sokáig lesz döntetlen az eredmény,jobb ha össze kapod magad!¤¤¤¤¤¤¤|")
      if computer<gamer:
        print('|>----------------------------------------------------------------------------<|')
        print("|Ne bízd el magd ,sokáig nem lesz így az állás!Nézzünk egy nehezebb feladványt!|")
      print('|>----------------------------------------------------------------------------<|')
      print(f'|Játék állás! ------->  Játékos  VS  Verhetetlen gép                           |')
      print(f'|                          {gamer}               {computer}                                <|||>')
      print('|>----------------------------------------------------------------------------<|')