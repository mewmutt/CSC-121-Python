# Myles Joubert
# Lab07P1.py
while True:
    phone_num = input("Enter phone number or q to quit: ")

    if phone_num == 'q' or phone_num == 'Q':
        break

    if phone_num.count('-') != 2:
        print("Phone number should have 2 dashes.")
        continue

    parts = phone_num.split('-')

    if not parts[0].isdigit() or int(parts[0]) < 200 or int(parts[0]) > 999:
        print("First 3 digits must be between 200 and 999.")
        continue
    if not parts[1].isdigit() or len(parts[1]) != 3:
        print("Second part of phone number must be a 3-digit number.")
        continue
    if not parts[2].isdigit() or len(parts[2]) != 4:
        print("Last part of phone number must be a 4-digit number.")
        continue
    formatted_num = parts[0] + '.' + parts[1] + '.' + parts[2]
    print("Phone number with dashes replaced:", formatted_num)