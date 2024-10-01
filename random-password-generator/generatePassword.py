import random
import string

def get_random_password(length, include_uppercase, include_digits, include_symbols):
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase if include_uppercase else ''
  digits = string.digits if include_digits else ''
  special = string.punctuation if include_symbols else ''
  
  full_string = lower + upper + digits + special
  
  if not full_string:
      raise ValueError("Parameters not passed properly.")
  
  password = ''.join(random.choice(full_string) for _ in range(length))
  
  return password


    