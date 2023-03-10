import os

filename = 'inventory.csv'

if not os.path.exists(filename):
    print(f'File {filename} not found')
    exit()

with open(filename, 'r') as f:
    for line in f:
        item_name, item_count, unit_price, description = line.strip().split(',')

        item_count = int(item_count)
        unit_price = float(unit_price)

        print(item_name)
        print(f"\t{item_count} in stock, ${unit_price:.2f}")
        print(f"\t{description}")
        print()


