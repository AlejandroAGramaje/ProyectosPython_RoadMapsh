import random

def random_number():
    return random.randint(1, 100)

def chances(difficulty):
    attempts_dict = {1: 10, 2: 5, 3: 3}
    
    if difficulty not in attempts_dict:
        print("Invalid difficulty level. Please choose 1 (Easy), 2 (Medium), or 3 (Hard).")
        return
    
    attempts = attempts_dict[difficulty]
    
    print(f"Great! You have selected difficulty level {difficulty}.\nLet's start the game!\n")
    
    number = random_number()
    contador = 0
    
    while contador < attempts:
        try:
            x = int(input("Enter your guess: "))
            contador += 1

            if x == number:
                print(f"🎉 Congratulations! You guessed the correct number in {contador} attempts.")
                break
            elif x < number:
                print(f"❌ Incorrect! The number is greater than {x}")
            else:
                print(f"❌ Incorrect! The number is less than {x}")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    else:
        print(f"Game Over! The correct number was {number}.")
