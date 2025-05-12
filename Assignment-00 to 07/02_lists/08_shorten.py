MAX_LENGTH = 4

def shorten(lst):
    """
    Shortens the provided list to a maximum length of 4 elements.
    """
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(f"List is too long. Removed the last element: {last_elem}")

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Note: parentheses are needed to call the function
    shorten(lst)
    print("Here is the shortened list:", lst)

if __name__ == "__main__":
    main()
