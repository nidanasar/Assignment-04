def add_many_numbrers(numbers: list[int]) -> int:
    """
    This function takes a list of numbers and returns their sum.
    """
    total_so_far = 0
    for number in numbers:
        total_so_far += number
    return total_so_far

def main():
   numbers= [1, 2, 3, 4, 5]
   print("The sum of the numbers is:", add_many_numbrers(numbers))
    # This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()