from math import sqrt  # Only import the sqrt function

def main():
    # Ask the user to enter the lengths of the two perpendicular sides
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Use the Pythagorean theorem to calculate the hypotenuse
    bc = sqrt(ab ** 2 + ac ** 2)

    # Print the result
    print("The length of BC (the hypotenuse) is:", bc)

# This runs the main() function
if __name__ == '__main__':
    main()
