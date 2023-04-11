# Myles Joubert
# 4/11/23
import sys
import random

def main():
    if len(sys.argv) != 4:
        print("Usage: python Lab12P1.py start end num_samples")
        return
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    num_samples = int(sys.argv[3])

    nums = list(range(start, end+1))
    sample_list = random.sample(nums, num_samples)

    print(f"Grabbing {num_samples} random numbers between {start} and {end}:")
    print(sample_list)

if __name__ == "__main__":
    main()