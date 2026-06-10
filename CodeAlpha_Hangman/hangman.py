import random

def play_hangman():
    print("Welcome to Hangman!")
    print("-------------------")
    
    word_bank = ["python", "coding", "program", "laptop", "matrix"]
    
    secret_word = random.choice(word_bank)
    
    guessed_letters = []
    
    incorrect_guesses_left = 6
    
    while incorrect_guesses_left > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word.strip()}")
        print(f"Incorrect guesses remaining: {incorrect_guesses_left}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word and won! 🎉")
            break
            
        guess = input("Guess a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print(f"⚠ You already guessed '{guess}'. Try a different letter.")
            continue
            
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            incorrect_guesses_left -= 1
            
    if incorrect_guesses_left == 0:
        print("\n💥 Game Over! You ran out of guesses.")
        print(f"The correct word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()