# adding values as lists in dict

count = int(input())

synonyms = {}
for i in range(count):
    key = input()
    value = input()
    if key not in synonyms:
        # create a key
        synonyms[key] = []
    # add values to the key in the form of a list
    synonyms[key].append(value)

for word, all_synonyms in synonyms.items():
    print(f"{word} - {', '.join(all_synonyms)}")