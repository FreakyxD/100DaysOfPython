from data_codec import encode_to_base64, decode_from_base64

# initialize save data
save_data = {
    "character_name": "Shyla",
    "level": 25,
    "inventory": ["sword", "shield", "flask", "cheese wheel"],
}


def read_savegame():
    try:
        with open("char1.sav", "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found!")
        exit()


def save_to_file(data):
    with open("char1.sav", "w") as file:
        file.write(data)


while True:
    user_choice = input("Choose an operation: encode or decode?").lower()

    if user_choice == "encode":
        print("⏳ encoding and saving file...")
        encoded_save = encode_to_base64(save_data)
        save_to_file(encoded_save)

    elif user_choice == "decode":
        encoded_save = read_savegame()
        print("⏳ reading and decoding file...")
        decoded_save = decode_from_base64(encoded_save)
        print(f"Decoded save: {decoded_save}")

    else:
        print("❌ not a valid choice")
