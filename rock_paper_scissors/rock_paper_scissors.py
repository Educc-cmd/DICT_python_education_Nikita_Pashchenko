import random

def get_user_name():
    user_name = input("Enter your name: ").strip()
    print(f"Hello, {user_name}")
    return user_name

def load_ratings():
    ratings = {}
    try:
        with open("rating.txt", "r") as file:
            for line in file:
                name, score = line.strip().split()
                ratings[name] = int(score)
    except FileNotFoundError:
        pass
    return ratings

def get_game_options():
    user_input = input("Enter game options separated by commas (or press Enter for default): ").strip()
    return user_input.split(",") if user_input else ["rock", "paper", "scissors"]

def determine_winner(user_choice, computer_choice, options):
    if user_choice == computer_choice:
        return "draw"
    
    index = options.index(user_choice)
    half = (len(options) - 1) // 2
    
    losing_options = options[index + 1:] + options[:index]
    winners = losing_options[-half:]
    
    return "win" if computer_choice in winners else "lose"

def game_loop(user_name, options, user_score, ratings):
    print("Okay, let's start")
    while True:
        user_choice = input("> ").strip().lower()
        
        if user_choice == "!exit":
            print("Bye!")
            break
        elif user_choice == "!rating":
            print(f"Your rating: {user_score}")
        elif user_choice in options:
            computer_choice = random.choice(options)
            result = determine_winner(user_choice, computer_choice, options)
            
            if result == "draw":
                print(f"There is a draw ({computer_choice})")
                user_score += 50
            elif result == "win":
                print(f"Well done. The computer chose {computer_choice} and failed")
                user_score += 100
            else:
                print(f"Sorry, but the computer chose {computer_choice}")
        else:
            print("Invalid input")

if __name__ == "__main__":
    user_name = get_user_name()
    ratings = load_ratings()
    user_score = ratings.get(user_name, 0)
    options = get_game_options()
    game_loop(user_name, options, user_score, ratings)
