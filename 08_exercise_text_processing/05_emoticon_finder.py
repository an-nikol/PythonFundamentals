text = input()


for idx in range(len(text)):
    emoticon = ':'
    if text[idx] == ':':
        emoticon += text[idx + 1]
        print(emoticon)
