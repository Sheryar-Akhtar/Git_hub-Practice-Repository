import random
import string


def generate_code(length=12):
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))


if __name__ == "__main__":
    code = generate_code()
    print("Your random test code:", code)
