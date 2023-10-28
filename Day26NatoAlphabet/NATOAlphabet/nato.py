import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Creating a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(nato_dict)

# Creating a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()

output = [nato_dict[letter] for letter in user_input]

print(output)
