import random

words =  ["cool","games","sunny","ali","shayan"]
word = random.choice(words)

hidden = ["_"] * len(word)
attempts = 6

print("Welcome to the Hangman Game")
print("You have to guessed the correct word in attempts", attempts, "attempts")

while attempts > 0:
    print("\nCurrent Word", " ".join(hidden))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = guess
            print("Correct Guess")
    else:
        attempts -=1
        print("Worng Guess attempts left", attempts)
        
    if "_" not in hidden:
            print("\nCongratulation You guessed the correct word", word)
            break

if "_" in hidden:
    print("\nGame Over! the correct word was", word)