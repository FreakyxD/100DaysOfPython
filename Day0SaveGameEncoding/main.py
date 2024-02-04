from data_codec import encode_to_base64, decode_from_base64

# initialize save data and filename
FILE_NAME = "char1.sav"
SAVE_DATA = {
    "character_name": "Shyla",
    "level": 25,
    "inventory": ["sword", "shield", "flask", "cheese wheel"],
}

# this is not great obfuscation, but serves as a proof of concept
OBFUSCATION = False


def read_savegame():
    try:
        with open(FILE_NAME, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found!")
        exit()


def save_to_file(data):
    with open(FILE_NAME, "w") as file:
        file.write(data)


while True:
    user_choice = input("Choose an operation: encode (e), decode (d), or quit (q)?").lower()

    if user_choice in ("encode", "e"):
        print("⏳ Encoding and saving file...")
        encoded_save = encode_to_base64(SAVE_DATA, OBFUSCATION)
        save_to_file(encoded_save)
    elif user_choice in ("decode", "d"):
        print("⏳ Reading and decoding file...")
        encoded_save = read_savegame()
        decoded_save = decode_from_base64(encoded_save, OBFUSCATION)
        print(f"Decoded save: {decoded_save}")
    elif user_choice in ("quit", "q"):
        print("Exiting program.")
        break
    else:
        print("❌ Not a valid choice. Please enter 'encode', 'decode', or 'quit'.")
