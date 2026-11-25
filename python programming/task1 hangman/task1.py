import random
hangman_word =[
    """
        ------
        |    |
        |
        |
        |
        |
       ----------
       """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ----------
    """,
]
words = ("python","programming","love","weekend")
max_wrong=len(hangman_word)-1
def hangman():
    word=random.choice(words)
    wrong=0
    guessed_letters= set()
    while wrong<max_wrong:
        print(hangman_word[wrong])
        print("Guess letters: ")
        display = print("  ".join(ch if ch in guessed_letters else "_" for ch in word))
        print(f"  Word: {display}")
        print(f"  Guessed: {', '.join(sorted(guessed_letters)) or 'none'}")
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word! the word was :)",word)
            break
        guess=input("Guess letters: ").lower().strip()
        if len(guess) !=1 or not guess.isalpha():
           print("Please enter a letter only")
           continue
        if guess in guessed_letters:
            print("You already guessed this letter")
            continue
        guessed_letters.add(guess)
        if guess not in word:
            wrong+=1
            print(f"wrong {max_wrong-wrong} guesses left")

    print(hangman_word[wrong])
    print("Game Over , the word was :",word)

if __name__ == "__main__":
    print("Welcome to Hangman")
    while True:
        hangman()
        play_again = input("Do you want to play again? (y/n): ").lower().strip()
        if play_again != "y":
            print("thank you for playing")
            break

