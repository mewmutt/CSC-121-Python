# Myles Joubert
# Lab06P2.py
import random

# Step a
num_values = int(input("How many values to put in the tuple? "))
start_range = int(input("What is the start of the range? "))
end_range = int(input("What is the end of the range? "))

# Step b
random_list = []
for i in range(num_values):
    random_list.append(random.randint(start_range, end_range))

random_tuple = tuple(random_list)

# Step c
print("Step c: Tuple of {} random numbers: {}".format(num_values, random_tuple))

# Step d
first_three = random_tuple[:3]
print("Step d: Tuple of first 3 numbers: {}".format(first_three))

# Step e
last_three = random_tuple[-3:]
print("Step e: Tuple of last 3 numbers: {}".format(last_three))

# Step f
concatenated_tuple = first_three + last_three
print("Step f: Two tuples concatenated: {}".format(concatenated_tuple))

# Step g
sorted_tuple = tuple(sorted(concatenated_tuple))
print("Step g: Two tuples concatenated and sorted: {}".format(sorted_tuple))