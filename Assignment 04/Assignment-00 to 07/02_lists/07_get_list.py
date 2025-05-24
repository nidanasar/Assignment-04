def main():
    lst=[]
    val=input("Enter a Value: ")
    while val:
        lst.append(val)
        val=input("Enter more values: ")
        print("Here we have the list: ", lst)


if __name__ == "__main__":
        main()