PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

# def main():
#     user_age: int = int(input("Please enter your age: "))
#     if user_age >= PETURKSBOUIPO_AGE:
#         print(f"You are eligible to vote in Peturksbouipo.the voting age is {PETURKSBOUIPO_AGE}.")
#     else:
#         print(f"You are not eligible to vote in Peturksbouipo. the voting age is {PETURKSBOUIPO_AGE}.")
#     if user_age >= STANLAU_AGE:
#         print(f"You are eligible to vote in Stanlau. The voting age is {STANLAU_AGE}.")
#     else:
#         print(f"You are not eligible to vote in Stanlau. the voting age is {STANLAU_AGE}.")
#     if user_age >= MAYENGUA_AGE:
#         print(f"You are eligible to vote in Mayengua. The voting age is {MAYENGUA_AGE}.")
#     else:
#         print(f"You are not eligible to vote in Mayengua. The voting age is {MAYENGUA_AGE}.")
# if __name__ == "__main__":
#     main()

def main():
    age = int(input("How old are you? "))

    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")

    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

if __name__ == "__main__":
    main()
