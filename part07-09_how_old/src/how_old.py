# Write your solution here
from datetime import datetime

# print("Please give your date of birth")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

dob = datetime(year, month, day)

millenium = datetime(1999, 12, 31)

difference = millenium - dob

if difference.days > 0:
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")