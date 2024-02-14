import random
import string

def generate_random_password(length=8):
    # Define characters for the password, including letters, digits, and special symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def is_acceptable_password(password, dictionary_words):
    # Check if the password has at least one special symbol
    has_special_symbols = any(char in string.punctuation for char in password)

    # Check if the password is not a word in the dictionary list
    is_not_dictionary_word = password.lower() not in dictionary_words

    # Return True if the password meets both criteria
    return has_special_symbols and is_not_dictionary_word

def password_simulator(iterations=40):
    accepted_passwords = []  # List to store accepted passwords
    dictionary_words = ["example", "password", "security", "admin"]  # List of dictionary words (replace with a more extensive list)

    # Iterate for the specified number of times
    for _ in range(iterations):
        generated_password = generate_random_password()

        # Check if the generated password is acceptable
        if is_acceptable_password(generated_password, dictionary_words):
            accepted_passwords.append(generated_password)
            print(f"Accepted Password: {generated_password}")
        else:
            print(f"Rejected Password: {generated_password}")

    print("\nAccepted Passwords:")
    for password in accepted_passwords:
        print(password)

# Example usage:
password_simulator()
