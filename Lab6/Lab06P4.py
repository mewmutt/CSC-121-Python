# Myles Joubert
# Lab06P4.py

import matplotlib.pyplot as plt

# Get input from the user
title = input("Enter the line graph title: ")
x_label = input("Enter the label for the x-axis: ")
y_label = input("Enter the label for the y-axis: ")

labels = []
values = []

for i in range(5):
    tick_label = input("Enter the name for tick {}: ".format(i+1))
    tick_value = float(input("Enter the value for tick {}: ".format(i+1)))
    labels.append(tick_label)
    values.append(tick_value)

# Create the line graph
plt.plot(labels, values, '-o')

# Add title and axis labels
plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)

# Set the tick marks on the x-axis
plt.xticks(labels)

# Add grid lines
plt.grid()

# Display the line graph
plt.show()

# My system has been having errors with Matplotlib. therefore it will not work. But if you want to run my program then it will work. I apologize for the inconvinience. 