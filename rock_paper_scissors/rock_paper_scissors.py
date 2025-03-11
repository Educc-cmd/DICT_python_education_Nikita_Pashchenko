import random

# Отримуємо ім'я користувача
user_name = input("Enter your name: ").strip()
print(f"Hello, {user_name}")

# Завантажуємо рейтинг гравця
ratings = {}
try:
    with open("rating.txt", "r") as file:
        for line in file:
            name, score = line.strip().split()
            ratings[name] = int(score)
except FileNotFoundError:
    pass

user_score = ratings.get(user_name, 0)

# Отримуємо опції гри
user_input = input("Enter game options separated by commas (or press Enter for default): ").strip()
options = user_input.split(",") if user_input else ["rock", "paper", "scissors"]
print("Okay, let's start")


def determine_winner(user_choice, computer_choice, options):
    if user_choice == computer_choice:
        return "draw"

    index = options.index(user_choice)
    half = (len(options) - 1) // 2


    losing_options = options[index + 1:] + options[:index]
    winners = losing_options[:half]  # Ті, хто перемагають user_choice

    return "win" if computer_choice in winners else "lose"


# Основний цикл гри
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
