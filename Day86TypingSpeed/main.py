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
debug_word_list = [
    'list', 'voice', 'war', 'array', 'output', 'log', 'return', 'debug', 'test',
    'execute', 'overflow', 'compile', 'trace', 'stack', 'variable', 'input',
    'code', 'module', 'exception', 'parameter', 'process', 'loop', 'syntax',
    'breakpoint', 'function', 'condition'
]

# Create the main window
root = tk.Tk()
root.title("test")

# UI Elements
label_font = ("Menlo", 24)  # Font family and size
text_font = ("Menlo", 24)  # Font family and size

label = tk.Label(root, text="0", font=label_font)
label.pack(pady=10)

text_field = tk.Text(root, height=3, width=50, font=text_font, wrap=tk.WORD)
text_field.pack(pady=10, expand=True, fill=tk.BOTH)

# Global tkinter variable to control flow
correct_key_pressed = tk.BooleanVar()


def pop_next_20_words(list1):  # todo update to 20 words
    return [list1.pop(0) for _ in range(min(2, len(list1)))]


def current_letter_correct(letter_to_check):
    # correct_key_pressed.set(False)  # fix not needed
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


def clear_text_field():
    text_field.config(state=tk.NORMAL)
    text_field.delete("1.0", tk.END)
    text_field.config(state=tk.DISABLED)


def add_markup(line, char_index, operation=None):
    """
    Adds markup to a specific character in the text field.

    Parameters:
    line (int): The line number where the character is located.
    char_index (int): The index of the character within the line.
    operation (str, optional): The type of markup to apply. Can be 'border' or 'mark'.

    Raises:
    ValueError: If an incorrect markup operation is provided.
    """
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


def insert_all_words(words):
    text_field.config(state=tk.NORMAL)  # Enable the text field for editing

    first_word = True
    for i, word in enumerate(words):
        for letter in word:  # todo enumerate still needed?
            if first_word:
                insert_letter_at_end(letter, True)
                first_word = False
            else:
                insert_letter_at_end(letter, False)
        if i < len(words) - 1:  # Only add a space if it's not the last word
            insert_letter_at_end(" ", False)

    text_field.config(state=tk.DISABLED)  # Disable the text field after inserting


def index_to_letter(curr_index, line):
    full_string_start = f"{line}.{curr_index}"
    full_string_end = f"{line}.{curr_index + 1}"

    letter = text_field.get(full_string_start, full_string_end)  # "1.0" means start at line 1, character 0
    return letter


# main logic
while True:
    if not debug_word_list:
        print("No more words to process. Exiting the loop.")
        break

    next_words = pop_next_20_words(debug_word_list)
    print("Next words:", next_words)
    print("Remaining words:", debug_word_list)

    if not next_words:
        print("No next words retrieved. Exiting the loop.")
        break

    insert_all_words(next_words)

    # todo adjust for multiple lines
    content = text_field.get("1.0", "end-1c")  # Retrieve the content without the extra newline
    content_length = len(content)
    print("length: ", content_length)
    print("content:", repr(content))

    if content_length == 0:
        print("No content to process. Exiting the loop.")
        break

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

    clear_text_field()

# todo Speed calculation


# Unbind any residual key events
root.unbind("<KeyPress>")

# Start the Tkinter event loop
root.mainloop()
