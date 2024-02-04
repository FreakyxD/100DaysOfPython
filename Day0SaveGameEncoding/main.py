from data_codec import encode_to_base64

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


encoded_save = encode_to_base64(save_data)
save_to_file(encoded_save)
