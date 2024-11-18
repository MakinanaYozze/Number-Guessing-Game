import random 

numbers = list(range(1, 10))

target_number = random.choice(numbers)

print("Welcome to 'Guess the number'!")
print("I have chsen a number between 1 and 10.")
print("You have 3 attempts to guess it correctly.\n")
 
for attempt in range(1, 4):
    guess = int( input(f"Attempt {attempt}: Enter your guess: "))
    if guess == target_number:
        print("Great! You guessed the correct number!")
        break 
    elif guess < target_number:
        print("Too low! Try again.")
        
else:
    print(f"Sorry, you are out of attempts! The correct number was {target_number}.")