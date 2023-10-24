text = input().lower()
words = ['sand', 'water', 'fish', 'sun']
# sum - returns the sum of all items in an iterable
# text.count(word) function returns the number of times a word from the list words is mentioned
# for word in words - iterates over the list
print(sum([text.count(word) for word in words]))
