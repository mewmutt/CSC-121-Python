# Myles Joubert
# 1/24/23
# Lab04P3
import random

def spin_wheel(spins):
    for i in range(1, spins+1):
        spin = random.randint(1, 16)
        if spin == 16:
            print(f"Spin {i}: {spin} ==> JACKPOT!")
        elif spin % 3 == 0:
            print(f"Spin {i}: {spin} ==> Green")
        elif spin % 3 == 1:
            print(f"Spin {i}: {spin} ==> Yellow")
        else:
            print(f"Spin {i}: {spin} ==> Red")
    print("Thanks for playing!")

def main():
    spins = int(input("How many times do you want to spin the wheel? "))
    while spins < 4 or spins > 10:
        spins = int(input("Enter a number between 4 and 10: "))
    spin_wheel(spins)

main()