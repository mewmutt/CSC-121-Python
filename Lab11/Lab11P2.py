#
# Myles Joubert
# 4/2/23
# Classes and OO Programming - Problem 2
#
import pickle
from inventory_item import InventoryItem

def main():
    inventory = load_inventory()
    display_inventory(inventory)

answer = ''
while answer.lower() != 'n':

    item = InventoryItem()
    item.set_item_name(input('Enter the item name: '))
    item.set_count(int(input('Enter the item count: ')))
    item.set_unit_cost(float(input('Enter the unit cost: ')))
    item.set_description(input('Enter the description: '))


    inventory.append(item)

    answer = input('Do you want to enter more items? ')

    display_inventory(inventory)
    save_inventory(inventory)


def load_inventory():
    inventory = []
    try:
        with open("inventory.dat", "rb") as file:
            inventory = pickle.load(file)
    except FileNotFoundError:
        pass
    return inventory

def save_inventory(inventory):
    with open("inventory.dat", "wb") as file:
        pickle.dump(inventory, file)
    print('Inventory.dat file was created.')

def display_inventory(inventory):
    print()
    print('Current Inventory')
    print('-----------------')
    if len(inventory) == 0:
        print('Inventory is empty.')
    else:
        for item in inventory:
            print(item)
    print()

if __name__ == '__main__':
    main()