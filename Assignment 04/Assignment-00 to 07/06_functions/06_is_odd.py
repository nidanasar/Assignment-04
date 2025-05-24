def main():
    for i in range(10):
        if is_odd(i):
            print("odd")
        else:
            print("even")

def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False
    
if __name__ == '__main__':
    main()