import random
import string

def generate_random_password(length=12):
    """Generate a strong random password with letters, digits and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_readable_password(num_words=3):
    """Generate a readable password using common words and some digits/symbols."""
    words = ["tree", "apple", "code", "magic", "space", "light", "earth", "storm", "river", "wolf"]
    password = '-'.join(random.choice(words).capitalize() for _ in range(num_words))
    number = str(random.randint(10, 99))
    symbol = random.choice("!@#$%^&*")
    return password + symbol + number

def main():
    print("\n Welcome to the Password Generator!\n")
    print("1. Generate Random Strong Password")
    print("2. Generate Readable Password")
    choice = input("\nChoose an option (1/2): ")

    if choice == '1':
        length = int(input("Enter password length (e.g., 12): "))
        password = generate_random_password(length)
        print(f"\n Your Strong Password: {password}")
    elif choice == '2':
        password = generate_readable_password()
        print(f"\n Your Readable Password: {password}")
    else:
        print("Invalid choice. Please run again.")

if __name__ == "__main__":
    main()

