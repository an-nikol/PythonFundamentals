searched_str = input()
main_str = input()

while searched_str in main_str:
    main_str = main_str.replace(searched_str, '')

print(main_str)
    