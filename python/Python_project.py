import random

def number_guessing_game() :
    print("Welcome to Number Guessing Game")
    print("I am thinking of a number between 1 and 100")

    computer_choice=random.randint(1,100)
    attempt=0
    correct_guessing=False

    while correct_guessing is False:

        try:
            user_guess=int(input("Enter your guess :"))
            attempt += 1

            if user_guess<1 or user_guess>100:
                print("Please enter the number between only 1 to 100")
            elif computer_choice < user_guess:
                print("Too High!Try again")
            elif computer_choice > user_guess:
                print("Too Low!Try again")
            elif computer_choice == user_guess:
                print("Congratulations!You've guessed the correct number {} in {}".format(computer_choice,attempt))
                correct_guessing=True

        except ValueError:
            print("Error!Please enter only numbers")

number_guessing_game()
print("---------------Thank you---------------")