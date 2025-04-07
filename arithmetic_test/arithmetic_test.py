import random

def generate_question(level):
    if level == 1:
        num1, num2 = random.randint(2, 9), random.randint(2, 9)
        operator = random.choice(['+', '-', '*'])
        return f"{num1} {operator} {num2}", eval(f"{num1} {operator} {num2}")
    num = random.randint(11, 29)
    return f"{num}", num ** 2

def get_valid_input():
    while True:
        user_input = input("> ")
        if user_input.lstrip('-').isdigit():
            return int(user_input)
        print("Incorrect format.")

def get_level():
    while True:
        level = input("Which level do you want? Enter 1 or 2:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> ")
        if level in ("1", "2"): return int(level)
        print("Incorrect format.")

def main():
    level, correct_answers = get_level(), 0
    for _ in range(5):
        question, correct_answer = generate_question(level)
        print(question)
        correct_answers += get_valid_input() == correct_answer
        print("Right!" if get_valid_input() == correct_answer else "Wrong!")
    
    print(f"Your mark is {correct_answers}/5.")
    if input("Would you like to save your result to the file? Enter yes or no.\n> ").strip().lower() in ("yes", "y"):
        name = input("What is your name?\n> ")
        desc = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
        with open("results.txt", "a") as file:
            file.write(f"{name}: {correct_answers}/5 in level {level} ({desc}).\n")
        print("The results are saved in \"results.txt\".")

if __name__ 
