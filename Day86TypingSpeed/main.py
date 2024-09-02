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

# Create the main window
root = tk.Tk()
root.title("test")

# UI Elements
label_font = ("Helvetica", 24)  # Font family and size
text_font = ("Helvetica", 24)  # Font family and size

label = tk.Label(root, text="0", font=label_font)
label.pack(pady=10)

text_field = tk.Text(root, height=3, width=30, font=text_font)
text_field.pack(pady=10)

# Text field handling
# todo highlight also current letter
text_field.insert(tk.END, "test", "highlight")
text_field.insert(tk.END, " text ")
text_field.insert(tk.END, "hallo ")
text_field.config(state=tk.DISABLED)
text_field.tag_configure("highlight", background="teal", relief="raised")


# Input reader
def keydown(e):
    print('down', e.char)


root.bind("<KeyPress>", keydown)

# Speed calculation

# Start the Tkinter event loop
root.mainloop()
