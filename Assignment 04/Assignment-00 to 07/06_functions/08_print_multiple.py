def multiply(num:int):
    print("here is the multiplication table of", num)
    for i in range(num):
        curr_multiplier= i+1
        print(f"{num} * {curr_multiplier} = {num * curr_multiplier}")

def main():
    num=int(input("enter a number: "))
    multiply(num)

if __name__ == '__main__':
    main()