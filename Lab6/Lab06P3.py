# Myles Joubert
# Lab06P3.py

# Step a
list1 = [3, 1, 4, 1, 5]
list2 = [2, 5]

# Step b
list3 = [num*3-2 for num in range(5)]
print("Step b:", list3)

# Step c
list4 = [i-j for i in range(8) for j in range(4) if i % 2 == 1]
print("Step c:", list4)

# Step d
list5 = [i**i for i in list1]
print("Step d:", list5)

# Step e
list6 = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]
print("Step e:", list6)

# Step f
list7 = [list1[i] - list2[j] for i in range(len(list1)) for j in range(len(list2))]
print("Step f:", list7)

# Step g
list8 = [f"{list1[i]}&{list2[j]}" for i in range(len(list1)) for j in range(len(list2))]
print("Step g:", list8)