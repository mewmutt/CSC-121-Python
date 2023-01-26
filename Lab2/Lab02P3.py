# Myles Joubert  
# 1/13/2023
total_purchase = float(input("Enter the total purchase amount: "))
loyalty = input("Is the customer a loyalty program member (y/n): ")

discount = 0
if loyalty == "y":
    if total_purchase <= 100:
        discount = total_purchase * 0.15
    else:
        discount = total_purchase * 0.25
elif total_purchase > 100:
    discount = total_purchase * 0.05

total_after_discount = total_purchase - discount
sales_tax = total_after_discount * 0.06
total_after_tax = total_after_discount + sales_tax

print("Total after discount: $%.2f" % total_after_discount)
print("Sales tax: $%.2f" % sales_tax)
print("Total after tax: $%.2f" % total_after_tax)