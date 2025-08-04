# Password Generator – Python Project

## Project Roadmap

### Step 1: Set Up Project Directory

Create a folder and a Python file.

```
mkdir PasswordGeneratorProject
cd PasswordGeneratorProject
touch password_generator.py
```

### Step 2: Import Required Modules

In `password_generator.py`, import the necessary Python modules.

```python
import random
import string
```

### Step 3: Define Password Generator Functions

- `generate_random_password(length=12)`  
  Generates a strong password using uppercase, lowercase, digits, and special characters.

- `generate_readable_password(num_words=3)`  
  Generates an easy-to-remember password by combining readable words, a symbol, and a number.

### Step 4: Create User Interface (Terminal Based)

Use `input()` to allow the user to:
- Choose between strong and readable password.
- Specify password length (for strong password).

Display the generated password using `print()`.

### Step 5: Run the Script

Use the command below to run your Python program:

```
python3 password_generator.py
```

### Step 6: Example Output

```
1. Generate Random Strong Password
2. Generate Readable Password
Choose an option (1/2): 2
Your Readable Password: blue-moon-sky@32
```
