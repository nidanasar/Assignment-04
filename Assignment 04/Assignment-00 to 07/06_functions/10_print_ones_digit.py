def print_ones_digit(num):
    """
    Prints the ones digit of the given number.
    """
    ones_digit = num % 10
    print("The ones digit is", ones_digit)

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
