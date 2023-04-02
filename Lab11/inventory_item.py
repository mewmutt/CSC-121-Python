# Myles Joubert
# 4/2/23

class InventoryItem:
    def __init__(self, name, count, cost, description):
        self.name = name
        self.count = count
        self.cost = cost
        self.description = description

    def get_item_input(self):
        self.name = input("Enter the item name: ")
        while True:
            try:
                self.count = int(input("Enter the item count: "))
                break
            except ValueError:
                print("Invalid input, please enter an integer for the count.")
        while True:
            try:
                self.cost = float(input("Enter the item cost: "))
                break
            except ValueError:
                print("Invalid input, please enter a float for the cost.")
        self.description = input("Enter the item description: ")

    def __str__(self):
        return f"{self.name}\n\tCount: {self.count}, Cost: {self.cost:.2f}\n\t{self.description}"

