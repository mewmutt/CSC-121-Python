# Myles Joubert
# 4/10/23

import tkinter as tk

root = tk.Tk()
root.title("Cash Register")
root.geometry('250x150')

workbooks_label = tk.Label(root, text="Workbooks")
workbooks_entry = tk.Entry(root)
workbooks_entry.insert(0, "3")

textbooks_label = tk.Label(root, text="Textbooks")
textbooks_entry = tk.Entry(root)
textbooks_entry.insert(0, "5")

magazines_label = tk.Label(root, text="Magazines")
magazines_entry = tk.Entry(root)
magazines_entry.insert(0, "3")

discount_var = tk.IntVar()
discount_checkbutton = tk.Checkbutton(root, text="25% Discount", variable=discount_var)

total_label = tk.Label(root, text="Total")
total_value_label = tk.Label(root, text="$0.00")

calculate_button = tk.Button(root, text="Calculate")
quit_button = tk.Button(root, text="Quit")

workbooks_label.grid(row=0, column=0, sticky=tk.E)
workbooks_entry.grid(row=0, column=1)

textbooks_label.grid(row=1, column=0, sticky=tk.E)
textbooks_entry.grid(row=1, column=1)

magazines_label.grid(row=2, column=0, sticky=tk.E)
magazines_entry.grid(row=2, column=1)

discount_checkbutton.grid(row=3, column=0, columnspan=2)

total_label.grid(row=4, column=0, sticky=tk.E)
total_value_label.grid(row=4, column=1)

calculate_button.grid(row=5, column=0)
quit_button.grid(row=5, column=1)

def calculate_total():
    workbook_count = int(workbooks_entry.get())
    textbook_count = int(textbooks_entry.get())
    magazine_count = int(magazines_entry.get())
    total = workbook_count * 8.50 + textbook_count * 24.00 + magazine_count * 5.95
    if discount_var.get() == 1:
        total *= 0.75  # 25% discount.
    total_value_label.configure(text=f"${total:.2f}")

calculate_button.configure(command=calculate_total)
quit_button.configure(command=root.quit)

root.mainloop()
