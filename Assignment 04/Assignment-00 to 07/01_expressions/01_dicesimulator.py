# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 = random.randint(1, NUM_SIDES)  # First dice roll
    die2 = random.randint(1, NUM_SIDES)  # Second dice roll
    total = die1 + die2
    print("Total of two dice:", total)

def main():
    die1 = 10  # This die1 is just a variable in main
    print("die1 in main() starts as:", die1)
    
    # Call roll_dice() three times
    roll_dice()
    roll_dice()
    roll_dice()
    
    print("die1 in main() is:", die1)

# This line runs the main() function when the file is executed
if __name__ == '__main__':
    main()
