# There are 12 inches in 1 foot
INCHES_IN_FOOT = 12

def main():
    # Ask the user to enter number of feet
    feet = float(input("Enter number of feet: "))

    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT

    # Print the result
    print("That is", inches, "inches!")

# Call the main function to run the program
if __name__ == '__main__':
    main()
