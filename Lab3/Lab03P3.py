# Myles Joubert
# 1/23
# Bookstore Purchase Calculator with Data Validation

# Constants for the cost of each item type
WORKBOOK_COST = 8.50
TEXTBOOK_COST = 24.00
MAGAZINE_COST = 5.95

# Constants for the maximum number of each item type
MAX_WORKBOOKS = 40
MAX_TEXTBOOKS = 10
MAX_MAGAZINES = 25

# Get the number of workbooks being purchased
workbooks = int(input("Enter the number of workbooks: "))
while workbooks < 0 or workbooks > MAX_WORKBOOKS:
    print(f"Number of workbooks must be between 0 and {MAX_WORKBOOKS}.")
    workbooks = int(input("Enter the number of workbooks: "))

# Get the number of textbooks being purchased
textbooks = int(input("Enter the number of textbooks: "))
while textbooks < 0 or textbooks > MAX_TEXTBOOKS:
    print(f"Number of textbooks must be between 0 and {MAX_TEXTBOOKS}.")
    textbooks = int(input("Enter the number of textbooks: "))

# Get the number of magazines being purchased
magazines = int(input("Enter the number of magazines: "))
while magazines < 0 or magazines > MAX_MAGAZINES:
    print(f"Number of magazines must be between 0 and {MAX_MAGAZINES}.")
    magazines = int(input("Enter the number of magazines: "))
total_before_tax = (workbooks * WORKBOOK_COST) + (textbooks * TEXTBOOK_COST) + (magazines * MAGAZINE_COST)

sales_tax = total_before_tax * 0.07
total_after_tax = total_before_tax + sales_tax

print(f"Cost before tax: ${total_before_tax:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Cost after tax: ${total_after_tax:.2f}")