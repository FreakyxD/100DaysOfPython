import tkinter as tk

word_list = [
    "list", "voice", "war", "give", "direct", "wait", "you", "product", "eat", "simple",
    "full", "late", "by", "figure", "answer", "after", "why", "also", "science", "from",
    "step", "answer", "stood", "time", "example", "sentence", "sleep", "paper", "yet",
    "money", "draw", "simple", "is", "contain", "an", "fine", "why", "tail", "remember",
    "early", "standard", "add", "at", "could", "common", "look", "such", "north", "need",
    "talk", "will", "all", "those", "round", "dark", "fact", "your", "first", "inch",
    "force", "and", "east", "our", "end", "deep", "front", "hot", "small", "thousand",
    "man", "day", "early", "over", "decide", "appear", "distant", "early", "care",
    "inch", "love", "one", "why", "if", "children", "mean", "person", "should", "home",
    "need", "three", "father", "off", "self", "back", "like", "know", "ever", "rock",
    "out", "produce", "stay", "possible", "toward", "but", "stop", "live", "find",
    "differ", "fact", "distant", "something", "watch", "fish", "deep", "street",
    "record", "food", "animal", "round", "low", "feel", "even", "paper", "course",
    "note", "noun", "any", "snow", "off", "sentence", "such", "where", "full", "box",
    "about", "happen", "let", "star", "toward", "so", "why", "ease", "map", "something",
    "build", "said", "road", "will", "toward", "dry", "less", "fact", "sit", "science",
    "than", "wait", "land", "box", "too", "very", "now", "second", "find", "friend",
    "early", "got", "nothing", "less", "make", "horse", "me", "mind", "voice", "wheel",
    "year", "game", "product", "all", "do", "three", "appear", "start", "their", "clear",
    "these", "sun", "between", "earth", "class", "plane", "distant", "must", "produce",
    "also", "side", "numeral", "can", "mean", "paint", "spell", "would", "family",
    "machine", "don't", "now", "hard", "by", "head", "hot", "power", "figure", "go",
    "story", "heard", "stand", "tree", "think", "both", "car", "to", "among", "ready",
    "heard", "why", "object", "bed", "during", "done", "well", "when", "since", "again",
    "wood", "answer", "here", "surface", "mineral", "often", "start", "hear", "large",
    "stay", "boy", "build", "water", "while", "together", "usual", "stand", "an",
    "against", "then", "house", "nine", "world", "has", "place", "simple", "war",
    "ready", "draw", "some", "off", "let", "stop", "while", "time", "small", "land",
    "enough", "against", "will", "little", "eat", "build", "door", "paper", "face",
    "nothing", "much", "home", "my", "any", "move", "form", "again", "interest",
    "found", "test", "draw", "do", "close", "listen", "develop", "blue", "turn",
    "over", "paper", "tree", "use"
]
debug_word_list = ["list", "voice", "war"]

# Create the main window
root = tk.Tk()
root.title("test")

# UI Elements
label_font = ("Menlo", 24)  # Font family and size
text_font = ("Menlo", 24)  # Font family and size

label = tk.Label(root, text="0", font=label_font)
label.pack(pady=10)

text_field = tk.Text(root, height=3, width=30, font=text_font)
text_field.pack(pady=10)

# Global tkinter variable to control flow
correct_key_pressed = tk.BooleanVar()


def current_letter_correct(letter_to_check):
    def keydown(e):
        pressed_key = e.char
        print(f"{pressed_key} pressed!")
        compare(pressed_key)

    def compare(pressed_key):
        if pressed_key == letter_to_check:
            print("✅ Correct Key")
            correct_key_pressed.set(True)  # Mark as correct
        else:
            print("❌ Incorrect Key")
            correct_key_pressed.set(False)  # Mark as incorrect

        # After comparison, stop waiting for the key
        root.unbind("<KeyPress>")

    # Bind the key press event
    root.bind("<KeyPress>", keydown)

    # Wait until the correct_key_pressed variable changes (a key was pressed)
    root.wait_variable(correct_key_pressed)  # This will block until a key press
    return correct_key_pressed.get()  # Return True if correct, False otherwise


def insert_letter_at_end(letter_to_insert, to_highlight):
    if to_highlight:
        text_field.insert(tk.END, letter_to_insert, "border")
        text_field.tag_configure("border", relief="raised", borderwidth=2)
    else:
        text_field.insert(tk.END, letter_to_insert)


def add_markup(line, char_index, operation=None):
    text_field.config(state=tk.NORMAL)

    index_start = f"{line}.{char_index}"
    index_end = f"{line}.{char_index + 1}"

    if operation == "border":
        text_field.tag_add("border", index_start, index_end)
        text_field.tag_configure("border", relief="raised", borderwidth=2)
    elif operation == "mark":
        text_field.tag_add("mark", index_start, index_end)
        text_field.tag_configure("mark", relief="raised", borderwidth=2, background="red")
    else:
        raise ValueError(f"Incorrect markup operation at line {line}, char {char_index}")

    text_field.config(state=tk.DISABLED)


def remove_markup(line, char_index):
    # Define the start and end index of the current letter
    start_index = f"{line}.{char_index}"
    end_index = f"{line}.{char_index + 1}"

    text_field.tag_remove("border", start_index, end_index)
    text_field.tag_remove("mark", start_index, end_index)


def insert_all_words():
    first_word = True
    for word in debug_word_list:
        for index, letter in enumerate(word):  # todo enumerate still needed?
            if first_word:
                insert_letter_at_end(letter, True)
                first_word = False
            else:
                insert_letter_at_end(letter, False)
        insert_letter_at_end(" ", False)  # space between words
    text_field.config(state=tk.DISABLED)


def index_to_letter(curr_index, line):
    full_string_start = f"{line}.{curr_index}"
    full_string_end = f"{line}.{curr_index + 1}"

    letter = text_field.get(full_string_start, full_string_end)  # "1.0" means start at line 1, character 0
    return letter


# main logic
insert_all_words()

content = text_field.get("1.0", tk.END)  # Retrieve the content
content_length = len(content.strip())  # Strip any trailing newlines and spaces, then get length
print("length: ", content_length)

for index_current_letter in range(0, content_length):
    current_letter = index_to_letter(index_current_letter, 1)  # todo dynamic line handling
    print("will check for letter: ", current_letter)

    # keep letter highlight
    add_markup(line=1, char_index=index_current_letter, operation="border")

    correct = False
    while not correct:
        if current_letter_correct(current_letter):
            correct = True
            remove_markup(line=1, char_index=index_current_letter)
        else:
            # keep letter red
            add_markup(line=1, char_index=index_current_letter, operation="mark")

# todo Speed calculation

# Start the Tkinter event loop
root.mainloop()
