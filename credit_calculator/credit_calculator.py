import math
import argparse

parser = argparse.ArgumentParser(description="Credit calculator")
parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment: 'annuity' or 'diff'")
parser.add_argument("--payment", type=float, help="Monthly payment amount")
parser.add_argument("--principal", type=float, help="Loan principal")
parser.add_argument("--periods", type=int, help="Number of months")
parser.add_argument("--interest", type=float, help="Loan interest (annual, without % symbol)")

args = parser.parse_args()

parameters = [args.principal, args.payment, args.periods, args.interest]

if args.type not in ["annuity", "diff"]:
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
elif any(x is not None and x < 0 for x in parameters):
    print("Incorrect parameters")
elif sum(x is not None for x in parameters) < 3:
    print("Incorrect parameters")
else:
    i = args.interest / (12 * 100)

    if args.type == "diff":
        total_payment = 0
        for m in range(1, args.periods + 1):
            d = math.ceil((args.principal / args.periods) + i * (args.principal - (args.principal * (m - 1) / args.periods)))
            total_payment += d
            print(f"Month {m}: payment is {d}")
        overpayment = int(total_payment - args.principal)
        print(f"\nOverpayment = {overpayment}")

    elif args.type == "annuity":
        if args.principal is not None and args.periods is not None:
            annuity_payment = math.ceil(args.principal * (i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1))
            print(f"Your annuity payment = {annuity_payment}!")
            overpayment = int(annuity_payment * args.periods - args.principal)
            print(f"Overpayment = {overpayment}")

        elif args.payment is not None and args.periods is not None:
            principal = math.floor(args.payment / ((i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1)))
            print(f"Your loan principal = {principal}!")
            overpayment = int(args.payment * args.periods - principal)
            print(f"Overpayment = {overpayment}")

        elif args.principal is not None and args.payment is not None:
            n = math.log(args.payment / (args.payment - i * args.principal), 1 + i)
            n = math.ceil(n)
            years = n // 12
            months = n % 12

            if years == 0:
                print(f"It will take {months} months to repay this loan!")
            elif months == 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")

            overpayment = int(args.payment * n - args.principal)
            print(f"Overpayment = {overpayment}")