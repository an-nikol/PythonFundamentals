import re

text = input()

pattern = r'([\=\/])([A-Z]{1,}[A-Za-z]{2,})\1'
matches = re.finditer(pattern, text)
travel_points = 0
destinations = []
for match in matches:
    curr_destination = match.group(2)
    travel_points += len(curr_destination)
    destinations.append(curr_destination)


print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
