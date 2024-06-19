import random

def get_word():
  while True:
    sel = input("wordbank or diy? ")
    if sel == "diy":
      chosenword = input("enter 6 letter word: ")
      if len(chosenword) != 6:
        print("make it 6 letters long.")
      else:
        return chosenword.lower()
    elif sel == "wordbank":
      words = ["babies", "packed", "eagles", "labels", "pacify", "oatfish", "iambus"]
      return random.choice(words).lower()
    else:
      print("not an option. try again.")
def play_hangman():
  """Main game loop"""
  guessed_letters = []
  turns = 5
  hidden_word = "_" * len(chosen_word)
  while turns > 0:
    print("Word:", hidden_word.replace("_ ", " "))
    guess = input("Enter guess: ").lower()
    if not guess.isalpha():
      print("Invalid guess. Please enter a letter.")
      continue
    elif guess in guessed_letters:
      print("You already guessed that letter.")
      continue
    guessed_letters.append(guess)
    if guess in chosen_word:
      new_hidden_word = ""
      for i, letter in enumerate(chosen_word):
        new_hidden_word += letter if letter in guessed_letters else "_"
      hidden_word = new_hidden_word
      print("right! u have", turns, " turns left.")
    else:
      turns -= 1
      print("wrong. u have", turns, " turns left.")
    if all(letter in guessed_letters for letter in chosen_word):
      print("congrats! correct!")
      break
  if turns == 0:
    print("so bad no more turns. word was:", chosen_word)
chosen_word = get_word()
play_hangman()
play_again = input("play again? yes/no: ")
if play_again.lower() == "yes":
  pass
