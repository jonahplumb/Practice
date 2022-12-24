#!/usr/bin/python3

import random

# Base Deck
deck = [2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 'J','Q','K','A', 'J','Q','K','A', 'J','Q','K','A', 'J','Q','K','A']

player = [] # Player hand
dealer = [] # Dealer hand

# Generate the other decks
num_decks = 6
deck = deck * num_decks

# Shuffle cards
random.shuffle(deck)


def dealCards(play):
    # These steps are a bit redundant considering
    # I already shuffled deck, could have just used pop(0)
    card = random.choice(deck)
    play.append(card)
    deck.remove(card)

# Calculate the totals, accounts for the Ace 
def totals(play):
    total = 0
    faceCards = ['K','Q','J']
    for card in play:
        if card in range(1,11): # 2-10
            total += card
        elif card in faceCards: # K,Q,J
            total += 10
        else: # Ace
            if total > 11:
                total += 1
            else:
                total += 11
    return total

# Method for dealer showing his cards.
def dealerHand():
    if len(dealer) == 2:
        return dealer[0]
    elif len(dealer) > 2:
        return dealer[0],dealer[1]

# Reshuffle method, reshuffles cards after 75 hands in same deck
def reshuffle():
    deck = [2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 'J','Q','K','A', 'J','Q','K','A', 'J','Q','K','A', 'J','Q','K','A']
    # Generate the other decks
    num_decks = 6
    deck = deck * num_decks

    # Shuffle cards
    random.shuffle(deck)


hands = 0
stand = 0

while stand < 1: # Loop for player sitting at table, will exit game when player stands (stand = 1)
    for _ in range(2):
        # Deal player and dealer 2 cards
        dealCards(dealer)
        dealCards(player)
    
    # Game booleans signaling turns
    playerIn = True
    dealerIn = True
    
    x = 0 # Counter for player loop

    # Game Loop
    while playerIn or dealerIn: # Game Loop
        # Check for 21 off rip
        if totals(player) == 21:
            print(f"\nWinner Winner Chicken Dinner\nYou won with {','.join(str(x) for x in player)} for a total of 21.\nDealer had {','.join(str(x) for x in dealer)}\n")
            break
        elif totals(dealer) == 21:
            print(f"\nDealer won for a total of 21.\nDealer had {','.join(str(x) for x in dealer)}\n")
            break

        # If no winner off rip, continue on
        while x < 1: # Player turn loop, will exit until bust or player chooses to stand
            # Display cards to user
            print(f"\nThe Dealer currently is showing \n{dealer[0]} \n")
            print(f"You currently have \n{', '.join(str(x) for x in player)} \nfor a total of {totals(player)}.\n ")
            # Asking player after first two cards, hit or stay
            option = input("Enter \"s\" to stay\nEnter \"h\" to hit\n")
            option = option.lower() # Not needed but better for end user

            if option == 's':
                x += 1 # This will keep player loop from occuring again
                playerIn = False # Change value for larger game loop, signal the player is done, now onto dealer
                break # Will break out of player loop
            else:
                dealCards(player)
                if totals(player) == 21:
                    break # breaks the loop in case of winner
                if totals(player) > 21:
                    break # Break on Bust
        

        # Manual instructions for our dealer
        if totals(player) > 21:
            dealerIn = False
            break # breaks the loop in case of bust (over 21) from player
        elif totals(dealer) > totals(player) and len(player) == 2: # If dealers first two cards have more than player after stay, dealer won't hit
            dealerIn = False
            break
        elif totals(dealer) < totals(player): # Will force dealer to hit if his total is lower than players
            dealCards(dealer)
        elif totals(dealer) > 16: # Dealer stays if total is 17
            dealerIn = False 
        elif totals(dealer) == totals(player): # if totals same, attempt to beat user
            dealCards(dealer)
        else : # Else draw cards
            dealCards(dealer)
        if totals(dealer) >= 21:
            break # breaks the loop in case of bust or win (over/equal 21) from dealer
        

# Since my player and dealer hand lists had strings and ints
# I used ', '.join(str(x) for x in player) when printing to avoid ['J', 4, 8]

    # Calculating winners, and relative print statements
    if totals(player) > 21: # Player wins on 21
        print("\nBust!! Dealer wins this time.")
        print(f"You have {','.join(str(x) for x in player)} for a total of {totals(player)}.\n")
    elif totals(dealer) > 21: # Dealer wins on 21
        print(f"\nCongratulations, the dealer busts with {','.join(str(x) for x in dealer)} for a total of {totals(dealer)}\n")
    elif (21 - totals(dealer) < (21 - totals(player))): # Dealer wins on higher total (non bust)
        print("\nDealer wins this time.")
        print(f"Dealer had {','.join(str(x) for x in dealer)} for a total of {totals(dealer)}.\nWhile you had {','.join(str(x) for x in player)} for a total of {totals(player)}\n")
    elif (21 - totals(dealer) > (21 - totals(player))): # Player wins on higher total (non bust)
        print("\nCongrats, you got the best of the dealer this time.")
        print(f"Dealer had {','.join(str(x) for x in dealer)} for a total of {totals(dealer)}.\nand you had {','.join(str(x) for x in player)} for a total of {totals(player)}\n")
    elif (21 - totals(dealer) == (21 - totals(player))): # Draws like the wc lol
        print("\nDraw lol.")
        print(f"Dealer had {','.join(str(x) for x in dealer)} for a total of {totals(dealer)}.\nWhile you had {','.join(str(x) for x in player)} for a total of {totals(player)}.\n")
        

    # Ask user if they want to play another hand or stand
    standYesNo = input("Enter \"1\" to stand, to continue playing press enter\n")
    if standYesNo == '1':
        print("\nThank you for playing")
        stand += 1 # This will trigger game end and end loop
    else: 
        player = [] # Empty the hands
        dealer = [] # Empty the hands
    # Increase our hand counter
    hands += 1
    # If we play 75 hands in this deck, we'll reshuffle
    if hands > 74:
        reshuffle()




