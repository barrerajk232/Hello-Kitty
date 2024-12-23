import random

def hello_kitty_game():
    print("Welcome to the Hello Kitty Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    
    secret = random.randint(1, 10)
    attempts = 0
    guess = None
    
    while guess != secret:
        user_input = input("Take a guess, cutie: ")
        
        # Attempt to parse integer
        try:
            guess = int(user_input)
        except ValueError:
            print("Oops! That wasn't a number. Try again.")
            continue
        
        attempts += 1
        
        if guess < secret:
            print("Awww, too low, sweetie!")
        elif guess > secret:
            print("Oopsie, too high!")
        else:
            print(f"Yay! You got it in {attempts} tries. Great job, kitty-cat!")

if __name__ == "__main__":
    hello_kitty_game()
