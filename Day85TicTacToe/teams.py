class Teams:
    def __init__(self):
        self.player = ""
        self.cpu = ""
        self.cross = "❌"
        self.circle = "⭕"

    def set_shape(self):
        # prompt user until a valid choice was made
        while True:
            choice = input("Pick 'cross' or 'circle': ").lower()
            if choice == "cross" or choice == "x":
                self.player = self.cross
                self.cpu = self.circle
                break
            elif choice == "circle" or choice == "o":
                self.player = self.circle
                self.cpu = self.cross
                break
            else:
                print("Invalid choice, try again.")

    def print_teams(self):
        if self.player == "" and self.cpu == "":
            print("No team assigned yet.")
            return
        print("You: ", self.player, "CPU: ", self.cpu)
        return

    def get_player_shape(self):
        return self.player

    def get_cpu_shape(self):
        return self.cpu
