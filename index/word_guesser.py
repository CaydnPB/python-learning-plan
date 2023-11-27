import random

def choose_word():
    words = ["html", "css", "javascript", "sqlite", "sequelize", "express", "react", "node", "python"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    print("Welcome to the Word Guesser!")
    secret_word = choose_word()
    guessed_letters = []
    attempts = 0

    while True:
        current_display = display_word(secret_word, guessed_letters)
        print("Current Word:", current_display)
        
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("Enter a different letter.")
            elif guess in secret_word:
                guessed_letters.append(guess)
                print("Correct guess!")
            else:
                attempts += 1
                print("Incorrect guess. Try again.")
        else:
            print("Enter a single letter.")

        if set(guessed_letters) == set(secret_word):
            print("Congratulations! You guessed the word '" + secret_word + "'!")
            break

    print(f"Number of Attempts: {attempts}")

if __name__ == "__main__":
    main()
