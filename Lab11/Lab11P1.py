# Myles Joubert
#4/2/23

from inventory_item import InventoryItem

science_book = InventoryItem("Science Book", 10, 12.90, "Textbook for SCI 100")
math_book = InventoryItem("Math Book", 15, 13.95, "Activity book for K-3")
fiction_book = InventoryItem("Fiction Book", 32, 7.00, "Sci-fi classic")


user_book = InventoryItem("", 0, 0.0, "")
user_book.get_item_input()


print(science_book)
print(math_book)
print(fiction_book)
print(user_book)