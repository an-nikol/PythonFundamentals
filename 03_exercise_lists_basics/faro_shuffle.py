deck_of_card = input().split()
number_of_shuffles = int(input())

# set the number a for-loop to count the number of shuffles
for shuffle in range(number_of_shuffles):
    # find the middle of the deck
    middle_deck_shuffle = len(deck_of_card) // 2
    # mark the left and the right half
    left_part = deck_of_card[0:middle_deck_shuffle]
    right_part = deck_of_card[middle_deck_shuffle:]
    # create a list to store the shuffled cards
    deck_after_shuffling = []
    # just add the cards
    for card_index in range(len(left_part)):  # this might be right part as well
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    # for the next time shuffling I set the deck after shuffling for a starting point
    deck_of_card = deck_after_shuffling
print(deck_of_card)