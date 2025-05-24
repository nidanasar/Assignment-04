# Speed of light in meters per second
C = 299792458

def main():
    # Ask the user for mass in kilograms
    mass = float(input("Enter kilos of mass: "))

    # Calculate energy using E = m * c^2
    energy = mass * (C ** 2)

    # Show the calculation steps and result
    print("e = m * C^2...")
    print("m =", mass, "kg")
    print("C =", C, "m/s")
    print(energy, "joules of energy!")

# Run the main function
if __name__ == '__main__':
    main()
