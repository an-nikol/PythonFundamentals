list_of_words = input().split()
palindromes = []
palindrome_word = input()


for word in list_of_words:
    if word == ''.join(reversed(word)):
        palindromes.append(word)


count_of_palindromes = palindromes.count(palindrome_word)
print(palindromes)
print(f'Found palindrome {count_of_palindromes} times')


