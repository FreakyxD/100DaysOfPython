class Teams:
    def __init__(self):
        self.p1 = ""
        self.p2 = ""
        self.cross = "❌"
        self.circle = "⭕"

    def set_shape(self):
        # prompt user until a valid choice was made
        while True:
            choice = input("Pick 'cross' or 'circle': ").lower()
            if choice == "cross" or choice == "x":
                self.p1 = self.cross
                self.p2 = self.circle
                break
            elif choice == "circle" or choice == "o":
                self.p1 = self.circle
                self.p2 = self.cross
                break
            else:
                print("Invalid choice, try again.")

    def print_teams(self):
        if self.p1 == "" and self.p2 == "":
            print("No team assigned yet.")
            return
        print("You: ", self.p1, "CPU: ", self.p2)
        return

    def get_shapes(self):
        return self.p1, self.p2
