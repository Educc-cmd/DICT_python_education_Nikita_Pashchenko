import requests

base_currency = input("Please, enter your base currency code: ").lower()
url = f"http://www.floatrates.com/daily/{base_currency}.json"

try:
    response = requests.get(url)
    data = response.json()
except Exception as e:
    print("An error occurred while fetching exchange rates:", e)
    exit()

cache = {}

if 'usd' in data:
    cache['usd'] = data['usd']
if 'eur' in data:
    cache['eur'] = data['eur']

while True:
    target_currency = input("Enter the currency you want to exchange to (or press Enter to exit): ").lower()
    if target_currency == "":
        break

    amount_str = input("Enter the amount you want to exchange: ")
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        continue

    print("Checking the cache...")

    if target_currency in cache:
        print("It is in the cache!")
        rate = cache[target_currency]['rate']
    else:
        print("Sorry, but it is not in the cache!")
        if target_currency in data:
            rate = data[target_currency]['rate']
            cache[target_currency] = data[target_currency]
        else:
            print("Sorry, this currency is not available for exchange.")
            continue

    received_amount = amount * rate
    print(f"You received {received_amount:.2f} {target_currency.upper()}.")

print("Exchange session ended.")