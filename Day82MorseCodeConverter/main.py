from morse import morse_alphabet_conventional, morse_alphabet_fancy
from time import sleep


def get_user_input():
    user_input = input("Enter your text to be converted to morse alphabet:\n")
    return user_input.lower()


def main():
    while True:
        mode_select = input("Do you want to convert text to Morse in a (c)onventional or (f)ancy way?\nType 'exit' to "
                            "quit.\n")
        if mode_select.lower() == "c":
            convert_to_morse(get_user_input(), morse_alphabet_conventional)
        elif mode_select.lower() == "f":
            convert_to_morse(get_user_input(), morse_alphabet_fancy)
        elif mode_select.lower() == "exit":
            print("Exiting program.")
            break
        else:
            print("Please make a valid choice")


# verbose printing, delay to make it feel like a machine
def convert_to_morse(input_string, alphabet):
    for char in input_string:
        if char in alphabet:
            print(alphabet[char], end=" ", flush=True)
        else:
            print("ERROR", end=" ", flush=True)
        sleep(0.15)
    print("\n")


main()
