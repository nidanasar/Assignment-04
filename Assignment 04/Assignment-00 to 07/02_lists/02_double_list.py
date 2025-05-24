# This function is where the program starts
def main():
    # Step 1: We create a list of numbers
    numbers = [1, 2, 3, 4]  # This list contains four numbers

    # Step 2: We want to double each number in the list
    # We use a loop to go through each index (position) in the list
    for i in range(len(numbers)):  # len(numbers) gives us the length of the list (which is 4)
        # Get the current number at index i and double it
        numbers[i] = numbers[i] * 2  # Replace the old value with the new doubled value

    # Step 3: After the loop, we print the updated list
    print(numbers)  # This will show: [2, 4, 6, 8]

# This line tells Python to run the main() function when the file starts
if __name__ == '__main__':
    main()
