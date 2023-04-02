#
# Myles Joubert
# 03/29/2023
# Trish's Bookstore Inventory System
#
import pickle

# Review the main() function and update TODO sections.
# Do not change any other code within main().
def main():
    inventory_counts, inventory_costs, inventory_descriptions = read_inventory_file()

    print("Welcome to Trish's Inventory Input System")
    print("Current Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_descriptions)

    response = ''
    while response != '0':
        # Display the user menu
        print("What would you like to do?")
        print("(1) Add an item\n"
              "(2) Display an item\n"
              "(3) Delete an item\n"
              "(4) Display all inventory\n"
              "(0) Exit")

        response = input('Enter your choice: ')
        if response == "1":  # Add an item
            item_name, item_count, unit_cost, description = get_item_input()
            inventory_counts[item_name] = item_count
            inventory_costs[item_name] = unit_cost
            inventory_descriptions[item_name] = description
        elif response == "2":  # Display an item            
            item_name = input('Enter item name: ')
            if item_name in inventory_counts:
                print(f"{item_name}: {inventory_counts[item_name]} @ ${inventory_costs[item_name]:.2f} each")
                print(f"Description: {inventory_descriptions[item_name]}")
            else:
                print("Not found")
        elif response == "3":  # Delete an item
            item_name = input('Enter item name: ')
            if item_name in inventory_counts:
                del inventory_counts[item_name]
                del inventory_costs[item_name]
                del inventory_descriptions[item_name]
            else:
                print("Not found")
        elif response == "4":  # Display all inventory
            display_all_inventory(inventory_counts, inventory_costs, inventory_descriptions)
        elif response != "0":
            print("Invalid choice. Try again.\n")

    # Ready to exit the program, display and save inventory as last steps
    print("Final Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_descriptions)

    save_inventory_file(inventory_counts, inventory_costs, inventory_descriptions)


def display_all_inventory(inventory_counts, inventory_costs, inventory_descriptions):
    if not inventory_counts:
        print("== Empty ==")
    else:
        for item_name in inventory_counts:
            print(f"{item_name}: {inventory_counts[item_name]} @ ${inventory_costs[item_name]:.2f} each")
            print(f"Description: {inventory_descriptions[item_name]}")
            print()


def save_inventory_file(inventory_counts, inventory_costs, inventory_descriptions):
    with open("inventory.dat", "wb") as f:
        pickle.dump(inventory_counts, f)
        pickle.dump(inventory_costs, f)
        pickle.dump(inventory_descriptions, f)


def read_inventory_file():
    try:
        with open('inventory.dat', 'rb') as inventory_file:
            inventory_counts = pickle.load(inventory_file)
            inventory_costs = pickle.load(inventory_file)
            inventory_descriptions = pickle.load(inventory_file)
    except FileNotFoundError:
        inventory_counts = {}
        inventory_costs = {}
        inventory_descriptions = {}

    return inventory_counts, inventory_costs, inventory_descriptions

# This function is complete, no changes needed, but feel free to review
def get_item_input():
    # Get item name
    while True:
        item_name = input('Enter the item name: ')
        if ',' in item_name:
            print('Item names cannot contain commas.')
        else:
            break
    # Get item count
    while True:
        try:
            item_count = int(input('Enter the item count: '))
            if item_count < 0:
                print('Item count must be 0 or greater.')
            else:
                break
        except:
            print('Item count must be an integer.')
    # Get unit cost
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except:
            print('Unit cost must be an integer.')
    # Get description
    while True:
        description = input('Enter the description: ')
        if ',' in description:
            print('Descriptions cannot contain commas.')
        else:
            break
    return item_name, item_count, unit_cost, description


main()
