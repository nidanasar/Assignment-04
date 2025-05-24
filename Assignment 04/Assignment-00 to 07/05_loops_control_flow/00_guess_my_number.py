import random

def main():
    #Genenrate the secrete numbeer
    seceret_number=random.randint(1,99)
    print("I am thinking of a number between 1 and 99....")

    guess=int(input("enter your guess: "))
    while guess != seceret_number:
        if guess < seceret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        guess=int(input("enter your guess: "))

        print("Congratulations! You guessed the number.")

        print() # print a blank line
        guess=int(input("enter your guess: "))
    print("Congratulations! You guessed the number.")
    print("the number was",seceret_number)

# Python boilerplate.
if __name__ == '__main__':
    main()