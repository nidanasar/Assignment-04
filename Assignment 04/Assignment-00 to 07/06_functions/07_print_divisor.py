def divide_num(num:int):
    print("here is the divisor of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    num=int(input("enter a number: "))
    divide_num(num)

if __name__ == '__main__':
    main()