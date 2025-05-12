def main():
    # Ask user for the number to be divided
    dividend = int(input("Please enter an integer to be divided: "))

    # Ask user for the number to divide by
    divisor = int(input("Please enter an integer to divide by: "))

    # Calculate the result and remainder
    result = dividend // divisor
    remainder = dividend % divisor

    # Print the result
    print("The result of this division is", result, "with a remainder of", remainder)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
