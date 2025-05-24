def double(num:int):
    return num * 2

def main():
    num=int(input("Enter an integer to double: "))
    doubled = double(num)
    print(f"The double of {num} is {doubled}")

if __name__ == '__main__':
    main()
