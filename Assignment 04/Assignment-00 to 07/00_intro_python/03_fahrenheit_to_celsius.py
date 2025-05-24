def main():
    # Ask the user to enter temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert to Celsius using the formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Print the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")


    

# This line ensures the main function runs when the file is executed
if __name__ == '__main__':
    main()
# This program converts temperature from Fahrenheit to Celsius.