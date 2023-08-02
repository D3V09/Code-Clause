import string
import secrets

def generate_random_password(length=12):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


number = int(input("Enter the length of Password :- "))
if (7<=number<=12):
    random_password = generate_random_password(number)
    print(random_password)
else:
    print("** Enter the Valid length for Password **")

print("Thank you")