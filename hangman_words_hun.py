with open('hangman_words_hun.txt') as f:
    hangman_words_hun = f.readlines()
    hangman_words_hun = [x.rstrip() for x in hangman_words_hun]

