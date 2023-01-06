# Myles Joubert, 1/5/22

# Asks the user to enter the number of workbooks, textbooks, and magazines being purchased;
workbooks = int(input("Enter the number of workbooks: "))
textbooks = int(input("Enter the number of textbooks: "))
magazines = int(input("Enter the number of magazines: "))

# Calculates the total before tax;
total_before_tax = (workbooks * 8.50) + (textbooks * 24.00) + (magazines * 5.95)

# Calculates the amount of sales tax on the total;
sales_tax = total_before_tax * 0.06

# Calculates the total after tax;
total_after_tax = total_before_tax + sales_tax

# Outputs the total before tax, the sales tax, and the total after tax;
print(f"Total before tax: ${total_before_tax:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total after tax: ${total_after_tax:.2f}")