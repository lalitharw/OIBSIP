import random
import string

def GeneratePassword(length,chars,nums,syms):
    characters = ""

    if chars == "y":
        characters += string.ascii_letters
    if nums == 'y':
        characters += string.digits
    if syms == 'y':
        characters += string.punctuation

    password = ''

    for _ in range(length):
        password += random.choice(characters)
    

    print("="*int(length+20))
    print(f"Your password is: {password}")


length = int(input("Enter length of password: "))
chars = input("Do you want characters in your password?(Y/n) ").lower()
nums = input("Do you want numbers in your password?(Y/n) ").lower()
syms = input("Do you want symbols in your password?(Y/n) ").lower()


GeneratePassword(length,chars,nums,syms)