import hashlib
import string

def my_hash(login, length=12) :

    if login == 'q' :
        return 'q'

    hash_object = hashlib.sha256(login.encode())
    hex_dig = hash_object.hexdigest()

    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation
    all_chars = letters + digits + specials

    password_chars = []

    idx = 0
    while len(password_chars) < length:
        char_type = int(hex_dig[idx:idx+2], 16) % 3
        if char_type == 0:
            index = int(hex_dig[idx:idx+2], 16) % len(letters)
            password_chars.append(letters[index])
        elif char_type == 1:
            index = int(hex_dig[idx:idx+2], 16) % len(digits)
            password_chars.append(digits[index])
        else:
            index = int(hex_dig[idx:idx+2], 16) % len(specials)
            password_chars.append(specials[index])
        idx += 2
        if idx >= len(hex_dig):
            idx = 0

    order = sorted(range(len(password_chars)), key=lambda i: int(hex_dig[i*2:(i*2)+2], 16))

    shuffled_password_chars = [password_chars[i] for i in order]

    password = ''.join(shuffled_password_chars)

    return input(f"\nYour password is : {password}\n\nEnter 'q' to quit : ")
