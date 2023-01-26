# Myles Joubert
# 1/23
# Pretty Pattern Generator
#
# NOTE: With the range functions, you may use 
# one, two, or three parameters to accomplish 
# your task.

# Ask the user for the number of rows
rows = int(input("How many rows? "))
# Ask the user for the number of columns
columns = int(input("How many columns? "))

# Iterate over the rows.
for row in range(rows):
    for col in range(columns):
        if row % 2 == 0 and col % 2 == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print()