import hashlib
import string

def choose_login():
    logins = {
        0: "stop",
        1: "nassim.berkhli@outlook.com",
        2: "nassim.berkhli.ad@outlook.com",
        3: "nassimberkhli02@gmail.com",
        4: "h.muman@yahoo.fr"
    }

    print("Your logins :\n")
    for key, value in logins.items():
        print(f"{key}: {value}")

    choix = int(input("\nEnter the number : "))
    
    return logins[choix]

def generate_deterministic_password(login, length=12):
    
    if login == "stop":
        return
    
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
    
    print(f"\nYour password is : {password}\n\n")
    return password

login_chosen = choose_login()

while login_chosen != "stop":
    generate_deterministic_password(login_chosen)
    login_chosen = choose_login()