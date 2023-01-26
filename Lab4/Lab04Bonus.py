# Myles Joubert
# 1/24/23
# Lab04Bonus
import random

def spin_wheel(spins, pot):
    winnings = 0
    print(f"${pot:.2f} has been deposited with the bank.")
    for i in range(1, spins+1):
        spin = random.randint(1, 16)
        if spin == 16:
            winnings += 50
            print(f"Spin {i}: {spin} ==> JACKPOT!\n\tYou win ${50:.2f}!")
        elif spin % 3 == 0:
            winnings += 20
            print(f"Spin {i}: {spin} ==> Green\n\tYou win ${20:.2f}!")
        elif spin % 3 == 1:
            print(f"Spin {i}: {spin} ==> Yellow")
        else:
            winnings -= 25
            print(f"Spin {i}: {spin} ==> Red\n\tYou lose ${25:.2f}!")
    if winnings > 0:
        print(f"Collect ${winnings:.2f} at the cashier's window.")
    elif winnings == 0:
        print("Allthe money is gone.")
    else:
        print(f"You owe ${abs(winnings):.2f} to the bank!")
        print("Thanks for playing!")

def main():
    spins = int(input("How many times do you want to spin the wheel? "))
    while spins < 4 or spins > 10:
        spins = int(input("Enter a number between 4 and 10: "))
    pot = float(input("How much money are you betting? "))
    spin_wheel(spins, pot)

main()