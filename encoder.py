def print_menu():
    print(
        "Menu\n"  
        "-------------\n" 
        "1. Encode\n"  
        "2. Decode\n" 
        "3. Quit\n"
    )
    return input("Please enter an option: ")


def encode(str):
    encoded_password = ""
    for value in str:
        value = int(value) + 3
        if value > 9:
            value -= 10
        encoded_password = encoded_password + f"{value}"
    return encoded_password


def decode(str):
    pass


def main():

    while True:
        option = print_menu()

        if option == "1":
            string = encode(input("Please enter your passcode to encode: "))
            print("Your password has been encoded and stored!")

        elif option == "2":
            print(f"The encoded password is {string}, and the original password is {decode(string)}.")

        else:
            break


if __name__ == "__main__":
    main()
