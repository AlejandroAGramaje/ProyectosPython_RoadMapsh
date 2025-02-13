import game

def main():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
    
    while True:
        difficulty = int(input("Select difficulty (1: Easy, 2: Medium, 3: Hard): "))
        game.chances(difficulty)

        x = input("Do you want to play again? (yes/no): ").strip().lower()

        if x == "yes":
            pass
        elif x == "no":
            print("Thanks for playing")
            break
        else:
            print("Select a correct option")

if __name__ == "__main__":
    main()