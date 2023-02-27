#
# Myles Joubert
# 2/22/23
# Count uppercase letters in a string
import os

# DO NOT CHANGE ANY CODE IN THE MAIN FUNCTION
def main():
    try:
        input_file = open('strings.txt', 'r')  # Open a file for reading
        for line in input_file:  # Use a for loop to read each line in the file
            manipulate_text(line)
            print()
    except FileNotFoundError:
        print('Did not find strings.txt in current directory:')
        print(os.getcwd())


def manipulate_text(line):

    line = line.strip()
    print(line)

    if line.isupper():
        print("String is all uppercase.")
    elif line.islower():
        print("String is all lowercase.")
    elif line.isdigit():
        print("String is all digits.")

    x_count = line.count('X') + line.count('x')
    z_count = line.count('z') + line.count('Z')
    seven_count = line.count('7')
    print(f"The line has {x_count} X's")
    print(f"The line has {z_count} z's")
    print(f"The line has {seven_count} 7's")

    new_line = line + "<<< Test"
    print(new_line)

    print(f"The string has {len(new_line)} characters.")

main()
