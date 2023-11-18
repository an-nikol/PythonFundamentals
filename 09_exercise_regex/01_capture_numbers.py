import re

results = []

while True:
    line = input()
    if not line:
        break

    matches = re.findall(r'\d+', line)
    results.extend(matches)
print(f"{' '.join(results)}")

