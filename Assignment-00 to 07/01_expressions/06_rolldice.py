import random  # To use random numbers for simulating dice rolls

def main():
    print("Rolling two dice...")

    die1 = random.randint(1, 6)  # Roll first die (1 to 6)
    die2 = random.randint(1, 6)  # Roll second die (1 to 6)
    total = die1 + die2          # Add the values

    print("Die 1 rolled:", die1)
    print("Die 2 rolled:", die2)
    print("Total of both dice:", total)

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
