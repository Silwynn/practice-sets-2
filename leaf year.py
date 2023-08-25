def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Get user input
y = int(input("Enter a year: "))

if is_leap_year(y):
    print(f"{y} is a leap year.")
else:
    print(f"{y} is not a leap year.")
