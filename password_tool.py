import random
import string


def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def check_strength(password):

    has_upper = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_symbol = True

    # --- Step 3: Tally the score (un-indented out of the for loop) ---
    score = 0

    if len(password) >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    # --- Step 4: Return the strength rating ---
    if score == 4:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"


while True:
    try:
        length = int(input("Enter desired password length (minimum 4): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if length < 4:
        print("Length must be at least 4.")
        continue

    pw = generate_password(length)
    rating = check_strength(pw)
    print(f"Password: {pw} | Strength: {rating}")
    break
