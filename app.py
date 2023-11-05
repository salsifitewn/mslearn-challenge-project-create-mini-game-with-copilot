import random
# create a mini game rock paper scissors
# 1. Create a function that will ask the user for their input
# 2. Create a function that will generate a random choice for the computer
# 3. Create a function that will compare the user's input and the computer's choice
# 4. Create a function that will determine who is the winner
# 5. Create a function that will ask the user if they want to play again
# 6. Create a function that will run the game
# 7. Create a function that will print the score
# 8. Create a main function that will run the game

# Create a function that will ask the user for their input
def user_input():
    user_choice = input("Please enter your choice: ")
    return user_choice

# Create a function that will generate a random choice for the computer
def computer_choice():
    choice = random.randint(1, 3)
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    else:
        return "scissors"
# Create a function that will compare the user's input and the computer's choice
def compare(user, computer):
    if user == computer:
        return "tie"
    elif user == "rock":
        if computer == "paper":
            return "computer"
        else:
            return "user"
    elif user == "paper":
        if computer == "scissors":
            return "computer"
        else:
            return "user"
    elif user == "scissors":
        if computer == "rock":
            return "computer"
        else:
            return "user"
    else:
        return "invalid"

#  Create a function that will determine who is the winner
def winner(user, computer):
    if user == "user":
        print("You win!")
    elif user == "computer":
        print("You lose!")
    else:
        print("It's a tie!")
# Create a function that will ask the user if they want to play again
def play_again():
    answer = input("Do you want to play again? (y/n): ")
    return answer
# Create a function that will print the score
def score(user, computer):
    print(f"User: {user} vs Computer: {computer}")

#  Create a main function that will run the game
def main():
    user_score = 0
    computer_score = 0
    while True:
        user = user_input()
        computer = computer_choice()
        print(f"User: {user} vs Computer: {computer}")
        result = compare(user, computer)
        winner(result, computer)
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        score(user_score, computer_score)
        answer = play_again()
        if answer == "n":
            break

main();