# password_generator/utils.py
import random
import string


def generate_password(numbers, symbols, total_length):

    # Define character sets
    letters = string.ascii_letters
    nums = string.digits
    syms = string.punctuation

    # Calculate the number of letters needed
    letters_needed = total_length - numbers - symbols

    # Generate the password
    password = ''.join(random.choice(letters) for _ in range(letters_needed))
    password += ''.join(random.choice(nums) for _ in range(numbers))
    password += ''.join(random.choice(syms) for _ in range(symbols))

    # Shuffle the password characters
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)
