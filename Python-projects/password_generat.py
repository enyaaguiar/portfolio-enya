import random 
import string

def generator_password(size):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(size))
    return password
size = int(input("Type the password size: "))
generated_password = generator_password(size)
print("Generated Password:", generated_password)