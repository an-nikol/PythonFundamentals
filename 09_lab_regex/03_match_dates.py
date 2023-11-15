import re

text = input()

pattern = r'(?P<day>\d{2})([\./-])(?P<month>[A-Z][a-z][a-z])\2(?P<year>\d{4})'
matches = re.finditer(pattern, text)

for match in matches:
    data_match = match.groupdict()
    print(f"Day: {data_match['day']}, Month: {data_match['month']}, Year: {data_match['year']}")
