# Myles Joubert
# Lab06P1.py

# Step a: Ask the user to enter 3 test scores for Ashley
a_list = []
print("Please enter Ashley's scores one by one.")
for i in range(3):
    score = float(input("Enter a score: "))
    a_list.append(score)
print("Ashley's scores:", a_list)

# Step b: Ask the user to enter 4 test scores for Barb
b_list = []
print("\nPlease enter Barb's scores one by one.")
for i in range(4):
    score = float(input("Enter a score: "))
    b_list.append(score)
print("Barb's scores:", b_list)

# Step c: Ask the user to enter 3 test scores for Carl
c_list = []
print("\nPlease enter Carl's scores one by one.")
for i in range(3):
    score = float(input("Enter a score: "))
    c_list.append(score)
print("Carl's scores:", c_list)

# Step d: Create a copy of each list and construct a list of lists from them
all_scores = [a_list[:], b_list[:], c_list[:]]
print("\nAll scores:", all_scores)

# Step e: Add 3 extra points to every score in all_scores
for i in range(len(all_scores)):
    for j in range(len(all_scores[i])):
        all_scores[i][j] += 3
print("\nAll scores after extra point:", all_scores)

# Step f: Create a new list called max_scores that is the maximum of the extra credit test scores of the three students
max_scores = []
for student_scores in all_scores:
    max_scores.append(max(student_scores))
print("\nMaximum scores:", max_scores)

# Step g: Display the original lists that were created in Steps a, b, and c
print("\nOriginal Scores")
print("Ashley's scores:", a_list)
print("Barb's scores:", b_list)
print("Carl's scores:", c_list)