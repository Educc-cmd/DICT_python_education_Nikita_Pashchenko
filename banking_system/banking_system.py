import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS card (
    id INTEGER PRIMARY KEY,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
)
''')
conn.commit()

def luhn_checksum(number_without_checksum):
    digits = [int(d) for d in number_without_checksum]
    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return (10 - sum(digits) % 10) % 10

def is_luhn_valid(card_number):
    checksum = int(card_number[-1])
    return luhn_checksum(card_number[:-1]) == checksum

def generate_card_number():
    iin = "400000"
    while True:
        account_id = str(random.randint(0, 999999999)).zfill(9)
        partial_number = iin + account_id
        checksum = luhn_checksum(partial_number)
        card_number = partial_number + str(checksum)

        cur.execute("SELECT number FROM card WHERE number = ?", (card_number,))
        if not cur.fetchone():
            return card_number

def generate_pin():
    return str(random.randint(0, 9999)).zfill(4)

def create_account():
    card_number = generate_card_number()
    pin = generate_pin()
    cur.execute("INSERT INTO card (number, pin) VALUES (?, ?)", (card_number, pin))
    conn.commit()

    print("\nYour card has been created")
    print("Your card number:")
    print(card_number)
    print("Your card PIN:")
    print(pin)

def log_into_account():
    card_number = input("\nEnter your card number:\n> ")
    pin = input("Enter your PIN:\n> ")

    cur.execute("SELECT * FROM card WHERE number = ? AND pin = ?", (card_number, pin))
    result = cur.fetchone()
    if result:
        print("\nYou have successfully logged in!")
        account_menu(card_number)
    else:
        print("\nWrong card number or PIN!")

def add_income(card_number):
    try:
        income = int(input("\nEnter income:\n> "))
        cur.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (income, card_number))
        conn.commit()
        print("Income was added!")
    except ValueError:
        print("Invalid income value!")

def do_transfer(card_number):
    print("\nTransfer")
    target = input("Enter card number:\n> ")

    if target == card_number:
        print("You can't transfer money to the same account!")
        return

    if not is_luhn_valid(target):
        print("Probably you made a mistake in the card number. Please try again!")
        return

    cur.execute("SELECT number FROM card WHERE number = ?", (target,))
    if not cur.fetchone():
        print("Such a card does not exist.")
        return

    try:
        amount = int(input("Enter how much money you want to transfer:\n> "))
        cur.execute("SELECT balance FROM card WHERE number = ?", (card_number,))
        balance = cur.fetchone()[0]

        if balance < amount:
            print("Not enough money!")
            return

        cur.execute("UPDATE card SET balance = balance - ? WHERE number = ?", (amount, card_number))
        cur.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (amount, target))
        conn.commit()
        print("Success!")
    except ValueError:
        print("Invalid amount!")

def close_account(card_number):
    cur.execute("DELETE FROM card WHERE number = ?", (card_number,))
    conn.commit()
    print("\nThe account has been closed!")

def account_menu(card_number):
    while True:
        print("\n1. Balance")
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit")
        choice = input("> ")

        if choice == "1":
            cur.execute("SELECT balance FROM card WHERE number = ?", (card_number,))
            balance = cur.fetchone()[0]
            print(f"\nBalance: {balance}")
        elif choice == "2":
            add_income(card_number)
        elif choice == "3":
            do_transfer(card_number)
        elif choice == "4":
            close_account(card_number)
            break
        elif choice == "5":
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
conn.close()