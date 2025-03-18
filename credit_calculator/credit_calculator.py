def loan_calculator():
    principal = int(input("Enter the loan principal:\n> "))
    print("What do you want to calculate?")
    print("type \"m\" – for number of monthly payments,")
    print("type \"p\" – for the monthly payment:")
    choice = input("> ")

    if choice == "m":
        monthly_payment = int(input("Enter the monthly payment:\n> "))
        months = (principal + monthly_payment - 1) // monthly_payment  # Округлення вгору
        if months == 1:
            print("It will take 1 month to repay the loan")
        else:
            print(f"It will take {months} months to repay the loan")

    elif choice == "p":
        months = int(input("Enter the number of months:\n> "))
        base_payment = principal // months
        last_payment = principal - (months - 1) * base_payment
        if base_payment == last_payment:
            print(f"Your monthly payment = {base_payment}")
        else:
            print(f"Your monthly payment = {base_payment} and the last payment = {last_payment}.")


loan_calculator()
