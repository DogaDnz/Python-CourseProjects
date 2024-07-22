from replit import clear
# HINT: You can call clear() to clear the output in the console.
from logo import art
print(art)

offerings = {}

def ask_user():
    name = input("What is your name?: ")
    bid = float(input("What is the price for bid? "))  # Ensure bid is treated as a number
    offerings[name] = bid

ask_user()

while True:
    result = input("Is there another user you want to add? Type yes or no: ").lower()
    if result == "yes":
        clear()
        ask_user()
    elif result == "no":
        break
    else:
        print("Please type 'yes' or 'no'.")

# Find the maximum value and corresponding key
max_value = float('-inf')
max_key = None
for key, value in offerings.items():
    if value > max_value:
        max_value = value
        max_key = key

print(f"The winner is {max_key} with a bid of {max_value}.")
