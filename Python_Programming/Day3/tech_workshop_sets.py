day1 = set(input("Enter day1 email adresses: ").split())
day2 = set(input("Enter day1 email adresses: ").split())
day3 = set(input("Enter day1 email adresses: ").split())

day1 = {i.lower() for i in day1}
day2 = {i.lower() for i in day2}
day3 = {i.lower() for i in day3}

print("Unique Attendees count:",len(day1|day2|day3),(day1|day2|day3))
print("Attendees who attended all three days:",day1 & day2 & day3)
print("Attendees who attended exactly one day:",day1^day2^day3)
print("day1 and day2:",day1&day2)
print("day2 and day3:",day3&day2)
print("day1 and day3:",day1&day3)

