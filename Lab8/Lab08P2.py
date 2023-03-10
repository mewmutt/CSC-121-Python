# Myles Joubert
# 03/08/2023

import csv


def get_item_name():
    while True:
        item_name = input('Enter the item name: ')
        if ',' in item_name:
            print('Item names cannot contain commas.')
        else:
            return item_name


def get_item_count():
    while True:
        try:
            item_count = int(input('Enter the item count: '))
            if item_count < 0:
                print('Item count must be 0 or greater.')
            else:
                return item_count
        except ValueError:
            print('Item count must be an integer.')


def get_unit_cost():
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                return unit_cost
        except ValueError:
            print('Unit cost can only contain digits and a single decimal point.')


def get_description():
    while True:
        description = input('Enter the description: ')
        if ',' in description:
            print('Descriptions cannot contain commas.')
        else:
            return description


def write_inventory_file(inventory_list):
    with open('inventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for item_info in inventory_list:
            writer.writerow(item_info.split(','))
    print('The file inventory.csv was created.')


def main():
    inventory_list = []
    print("Welcome to Trish's Inventory Input System")

    while True:
        item_name = get_item_name()
        item_count = get_item_count()
        unit_cost = get_unit_cost()
        description = get_description()

        item_info = item_name + ',' + str(item_count) + ',' + \
                    str(unit_cost) + ',' + description
        inventory_list.append(item_info)

        answer = ''
        while answer != 'y' and answer != 'n':
            answer = input('Enter another item? (y/n) ')
            answer = answer.lower()
            if answer != 'y' and answer != 'n':
                print('Enter y or n to continue.')
        if answer == 'n':
            break

    write_inventory_file(inventory_list)


if __name__ == '__main__':
    main()