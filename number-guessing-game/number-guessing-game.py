import random

def play_game():
    secretNum = random.randint(1,100)
    attempts = 5
    while attempts > 0:
        userNum = int(input("Enter a number (1 - 100): "))
        if userNum == secretNum:
            print("Congratulations! You have guessed the right number\n")
            break
        elif userNum > secretNum:
            print("Too high!")
            attempts -= 1
            print(f"{attempts} attempts left\n")
        else:
            print("Too low!")
            attempts -= 1
            print(f"{attempts} attempts left\n")
    
    if attempts == 0 and userNum != secretNum:
        print(f"You lose the game the number was {secretNum}")
            
play_game()
