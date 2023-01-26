#
# Myles Joubert
# 1/25/23
# Number Analysis Program
#
import random

def main():
    # List to store numbers
    number_list = []

    # The user must enter an odd number here.
    number_count = int(input('How many numbers? '))
    while number_count % 2 != 1:  # Check the number is NOT odd
        print('Please enter an odd number.')
        number_count = int(input('How many numbers? '))

    for i in range(number_count):
        # Generate a random number between 1-100 inclusive
        number = random.randint(1, 100)
        print(f'Entry {i+1}: {number}')
        # append number to number_list
        number_list.append(number)

    def get_low(nums):
        return min(nums)
    def get_high(nums):
        return max(nums)
    def get_total(nums):
        return sum(nums)
    low = get_low(number_list)
    high = get_high(number_list)
    total = get_total(number_list)
    average = total/number_count

    # The median is the number that is directly in the middle of the
    # sorted list. Implement these three steps to get the median:
    number_list.sort()
    median_index = (len(number_list) - 1) // 2  # This will get the middle index
    median = number_list[median_index]

    print('--------------')
    print(f'Low: {low}')
    print(f'High: {high}')
    print(f'Total: {total:.2f}')
    print(f'Average: {average:.2f}')
    print(f'Median: {median}')

# Call the main function.
main()