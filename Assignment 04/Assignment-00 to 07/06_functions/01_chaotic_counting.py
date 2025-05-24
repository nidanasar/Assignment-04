def chaotic_counting():
    for i in range(10):
        curr_num= i+1
        if done():
            return curr_num
        print(curr_num)

def done():
    """
    Returns True if the user has finished counting, False otherwise.
    """
    response = input("Have you finished counting? (yes/no): ").strip().lower()
    return response == 'yes'

def main():
    print("Let's start counting!")
    chaotic_counting()
    print("Counting finished!")

if __name__ == '__main__':
    main()