# Myles Joubert
# 3/24/2023

import random

set1 = set(random.sample(range(1, 16), 5))
set2 = set(random.sample(range(1, 16), 5))

print(f"set1: {set1}")
print(f"set2: {set2}")

union_set = set1.union(set2)
print(f"\nUnion of set1 and set2: {union_set}")

intersection_set = set1.intersection(set2)
print(f"\nIntersection of set1 and set2: {intersection_set}")

difference_set = set1.difference(set2)
print(f"\nDifference of set1 and set2: {difference_set}")

symmetric_difference_set = set1.symmetric_difference(set2)
print(f"\nSymmetric difference of set1 and set2: {symmetric_difference_set}")

less_than_9_set = {n for n in union_set if n < 9}
print(f"\nLess than 9 in union of set1 and set2: {less_than_9_set}")