#
# Myles Joubert
# 1/25/23
#
import random

def main():
    # Step a: Ask the user how many numbers they want in the lists
    number_count = int(input('Step a: How many numbers in each list? '))

    # Step b: Generate and display the first list of random integers
    first_list = []
    for i in range(number_count):
        number = random.randint(1, 15)
        first_list.append(number)
    print(f'Step b: First list: {first_list}')

    # Step c: Generate and display the second list of random integers
    second_list = []
    for i in range(number_count):
        number = random.randint(1, 15)
        second_list.append(number)
    print(f'Step c: Second list: {second_list}')

    # Step d: Compare the elements in the two lists and display the larger number
    print('Step d:')
    print('Larger number in each comparison:')
    for i in range(number_count):
        if first_list[i] > second_list[i]:
            print(f'{first_list[i]} : First list')
        elif first_list[i] < second_list[i]:
            print(f'{second_list[i]} : Second list')
        else:
            print(f'{first_list[i]} : Both lists are equal')

    # Step e: Combine the lists and display the combined list
    combined_list = first_list + second_list
    print(f'Step e: Combined list: {combined_list}')

    # Step f: Sort the combined list in place and display the sorted list
    combined_list.sort()
    print(f'Step f: Sorted list: {combined_list}')

    # Step g: Use list slicing to display the first and last three elements in the list
    print(f'Step g:')
    print(f'First three elements: {combined_list[:3]}')
    print(f'Last three elements: {combined_list[-3:]}')

    # Step h: Generate 4 random integers and check if they are in the combined list
    print(f'Step h:')
    for i in range(4):
        number = random.randint(1, 15)
        index = combined_list.index(number) if number in combined_list else None
        if index is not None:
            print(f'{number} at index {index}')
            combined_list.remove(number)
        else:
            print(f'{number} not found in list')

    # Step i: Print the final list after elements may have been deleted
    print(f'Step i: Final list: {combined_list}')

# Call the main function
main()