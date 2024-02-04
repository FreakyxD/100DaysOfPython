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
    user_choice = input("Choose an operation: encode or decode?").lower()

    if user_choice == "encode" or user_choice == "e":
        print("⏳ encoding and saving file...")
        encoded_save = encode_to_base64(SAVE_DATA, OBFUSCATION)
        save_to_file(encoded_save)

    elif user_choice == "decode" or user_choice == "d":
        encoded_save = read_savegame()
        print("⏳ reading and decoding file...")
        decoded_save = decode_from_base64(encoded_save, OBFUSCATION)
        print(f"Decoded save: {decoded_save}")

    else:
        print("❌ not a valid choice")
