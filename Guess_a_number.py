import numpy as np

def randomNumber(level, N):
    
    # Setting number of attempts based on the difficulty level
    attempts_dict = {'Easy': 20, 'Medium': 15, 'Hard': 10}
    n = attempts_dict.get(level, None)
    
    if n is None:
        print("Invalid difficulty level. Please choose Easy, Medium, or Hard.")
        return
    
    print(f"You have {n} attempts to guess the number!")
    
    for attempt in range(1, n + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{n}: Make a guess (1-100): "))
            
            if guess < 1 or guess > 100:
                print("Out of bounds! Please guess a number between 1 and 100.")
                continue
            
            if guess == N:
                print(f"🎉 YOU WON! You guessed it in {attempt} attempts!")
                return
            
            # Provide feedback on the guess
            if abs(guess - N) <= 5:
                print("🔥 So close! Try again.")
            elif guess > N:
                print("Too high. ")
            else:
                print(" Too low.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    # If the loop completes, the user failed to guess the number
    print(f"💔 Sorry, you've used all your attempts. The correct number was {N}.")

def main():
    """Main function to run the Guess Game."""
    print('************** GUESS GAME **************')
    level = input("Choose a difficulty (Easy, Medium, or Hard): ").capitalize()
    N = np.random.randint(1, 101)  # Generates a random number between 1 and 100 (inclusive)
    randomNumber(level, N)

if __name__ == "__main__":
    main()
