
def select_cards(possible_cards, hand):
    i = 0
    for i, current_card in enumerate(possible_cards):
        print("Do you want to pick up {}?".format(current_card))
        answer = input()
        if answer.lower() == 'y':
            hand.append(current_card)
        i += 1

    if len(hand) < 3:
        print("You have too few cards in your hand. Please choose only 3.")
        return False
    elif len(hand) > 3:
        print("You have too many cards in your hand. Please choose only 3.")
        return False
    else:
        return True
    return hand


available_cards = ['queen of spades', '2 of clubs', '3 of diamonds', 'jack of spades', 'queen of hearts']

new_hand = select_cards(available_cards, [])

display_hand = "\n".join(new_hand)

print("Your new hand is: \n{}".format(display_hand))
