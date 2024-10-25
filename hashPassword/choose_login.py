def choose_login() :

    logins = {
        0: "quit",
        1: "nassim.berkhli@outlook.com",
        2: "nassim.berkhli.ad@outlook.com",
        3: "nassimberkhli02@gmail.com",
        4: "nassimberkhli02@gmail.com_wordreference"
    }

    print("\nYour logins :\n")
    for key, value in logins.items():
        print(f"{key}: {value}")

    choix = int(input("\nEnter the number : "))

    if choix == 0 :
        exit()

    return logins[choix]
