def main():
    # Define constants
    DAYS_IN_YEAR = 365
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60

    # Calculate seconds in a year
    seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

    # Display the result
    print("There are", seconds_in_year, "seconds in a year!")

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
