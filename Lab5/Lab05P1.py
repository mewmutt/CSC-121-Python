#
# Myles Joubert
# 1/25/23
# This program calculates the total cost for items purchased at Bargain
# Used Books. The program outputs the total cost before tax, the sales tax,
# and the total after tax.
#
TAX_RATE = 0.06  # 6% sales tax
WB_MAX = 40
WB_COST = 8.50
TB_MAX = 10
TB_COST = 24.00
MAG_MAX = 25
MAG_COST = 5.95

def get_item_count(max_allowed):
    item_count = int(input("Enter the number of items: "))
    while item_count < 0 or item_count > max_allowed:
        print("Number of items must be between 0 and {}".format(max_allowed))
        item_count = int(input("Enter the number of items: "))
    return item_count

def get_item_total(num_items, unit_price):
    return num_items * unit_price

def calc_and_display_receipt(wb_total, tb_total, m_total):
    subtotal = wb_total + tb_total + m_total
    tax = subtotal * TAX_RATE
    total = subtotal + tax
    if wb_total > 0:
        print("Workbooks: ${:.2f}".format(wb_total))
    if tb_total > 0:
        print("Textbooks: ${:.2f}".format(tb_total))
    if m_total > 0:
        print("Magazines: ${:.2f}".format(m_total))
    print("---------------------")
    print("Subtotal: ${:.2f}".format(subtotal))
    print("Tax: ${:.2f}".format(tax))
    print("Amount due: ${:.2f}".format(total))

def main():
    print('Workbooks')
    wb_item_count = get_item_count(WB_MAX)
    wb_total = get_item_total(wb_item_count, WB_COST)
    print('Textbooks')
    tb_item_count = get_item_count(TB_MAX)
    tb_total = get_item_total(tb_item_count, TB_COST)
    print('Magazines')
    m_item_count = get_item_count(MAG_MAX)
    m_total = get_item_total(m_item_count, MAG_COST)

    calc_and_display_receipt(wb_total, tb_total, m_total)


# Call the main function.
main()
