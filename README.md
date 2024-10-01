# Password Generator

A simple Python package for generating random passwords with customizable options.

## Features

- Generate random passwords with customizable length.
- Option to include/exclude uppercase letters, numbers, and special characters.
- Lightweight and easy to use. 

## Installation

To use the password generator, simply clone the repository and run the script:

```bash
git clone https://github.com/manogyaguragai/RandomPasswordPackage.git
cd RandomPasswordPackage

## Parameters
- length: The length of the password.
- include_upper: Whether to include uppercase letters.
- include_numbers: Whether to include digits (0-9).
- include_special: Whether to include special characters (e.g., !@#$%^&

## Usage Example

```python
from RandomPasswordGenPKG import get_random_password

password = get_random_password(length=10, include_upper=False, include_numbers=False, include_special=False)
print(f"Password: {password}")

## Contributing

Feel free to fork this repository and submit pull requests for any new features or improvements!

