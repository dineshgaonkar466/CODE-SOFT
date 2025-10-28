import random
import string

# Simple color combo
RED_ON_BLUE = "\033[31;44m"  # Red text on blue background
RESET = "\033[0m"            # Reset colors

print(RED_ON_BLUE + "\n==============================")
print("        PASSWORD GENERATOR")
print("==============================\n" + RESET)

count = 0

while True:
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be greater than 0. Try again.\n")
            continue
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()_+=-?/<>"

    all_chars = letters + numbers + symbols
    password = "".join(random.choice(all_chars) for _ in range(length))
    count += 1

    # Display password in red on blue
    print(RED_ON_BLUE + f"\nPassword #{count}: {password}\n" + RESET)

    again = input("Do you want to generate another password? (y/n): ").lower()
    if again != 'y':
        print(RED_ON_BLUE + "\nThank you for using the Password Generator!\n" + RESET)
        break
