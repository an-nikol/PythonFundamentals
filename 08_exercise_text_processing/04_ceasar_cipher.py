text = input()

encrypted_text = ''
for idx in range(len(text)):
    encrypted_text += chr((ord(text[idx])) + 3)
    text.replace(text[idx], encrypted_text)

print(encrypted_text)