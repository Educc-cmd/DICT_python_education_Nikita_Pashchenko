import random

accounts = {}

def generate_card_number():
    iin = "400000"
    while True:
        account_identifier = str(random.randint(0, 999999999)).zfill(9)
        card_number = iin + account_identifier
        if card_number not in accounts:
            break
    card_number += str(random.randint(0, 9))
    return card_number

def generate_pin():
    return str(random.randint(0, 9999)).zfill(4)

def create_account():
    card_number = generate_card_number()
    pin = generate_pin()
    accounts[card_number] = {"pin": pin, "balance": 0}
    print("\nYour card has been created")
    print("Your card number:")
    print(card_number)
    print("Your card PIN:")
    print(pin)

def log_into_account():
    card_number = input("\nEnter your card number:\n> ")
    pin = input("Enter your PIN:\n> ")
    if card_number in accounts and accounts[card_number]["pin"] == pin:
        print("\nYou have successfully logged in!")
        account_menu(card_number)
    else:
        print("\nWrong card number or PIN!")

def account_menu(card_number):
    while True:
        print("\n1. Balance")
        print("2. Log out")
        print("0. Exit")
        choice = input("> ")
        if choice == "1":
            print(f"\nBalance: {accounts[card_number]['balance']}")
        elif choice == "2":
            print("\nYou have successfully logged out!")
            break
        elif choice == "0":
            print("\nBye!")
            exit()

def main_menu():
    while True:
        print("\n1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        choice = input("> ")
        if choice == "1":
            create_account()
        elif choice == "2":
            log_into_account()
        elif choice == "0":
            print("\nBye!")
            break

main_menu()