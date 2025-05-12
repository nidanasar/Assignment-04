def main():
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

    # Ask the user for an adjective
    adjective = input("Please type an adjective and press enter: ")

    # Ask the user for a noun
    noun = input("Please type a noun and press enter: ")

    # Ask the user for a verb
    verb = input("Please type a verb and press enter: ")

    # Combine everything into a final sentence
    print(SENTENCE_START, adjective, noun, verb + "!")

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
