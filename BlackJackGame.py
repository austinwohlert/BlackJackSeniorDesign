# This is a blackjack game
# functions needed are below
# DONE will need a function for creating a deck
# DONE will need a function for adding up points in hand
# will need a function for displaying hands
# DONE will need a function for dealing cards
# will need a function for finding the best move
# possibly find a way to display info in a window and not textbox
from random import shuffle
import pygame
#import loadingandnaming
import imghdr
import os
pygame.init()

def deck():
    # deck joins the suits and ranks of a deck and then shuffles the deck into a random order
    deck = []
    for suit in ['H', 'S', 'C', 'D']:
        for rank in ['A', 'J', 'Q', 'K', '2', '3', '4', '5', '6', '7', '8', '9', 'T']:
            deck.append(suit+rank)
    shuffle(deck)
    return deck
def points(mycards):
    # Function points take in an argument called mycards. mycards will tally up the points in your hand
    # if you have a T J Q K in your hand it will add 10 points
    # if you have an ace in your hand it will give you 11 points if it helps or 1 if 11 will bust you
    my_points = 0
    ace_count = 0
    for i in mycards:
        if i[1] == 'J' or i[1] == 'Q' or i[1] == 'K' or i[1] == 'T':
            my_points += 10
        elif i[1] != 'A':
            my_points += int(i[1])
        else:
            ace_count += 1
    if ace_count == 1 and my_points <= 10:
        my_points += 11
    elif ace_count != 0:
        my_points += 1
    return int(my_points)

def create_hand(mydeck):
    # the create hand function will take in an argument called my deck
    # this function creates two hands my_hand and dealer_hand and returns them
    # my_hand will give you two cards
    # the dealer_hand will be created and made fully but not shown
    my_hand = []
    dealer_hand = []
    dealer_hand.append(mydeck.pop())
    dealer_hand.append(mydeck.pop())
    my_hand.append(mydeck.pop())
    my_hand.append(mydeck.pop())

    while points(dealer_hand) <= 16:
        dealer_hand.append(mydeck.pop())

    return [dealer_hand, my_hand]

game = ''
mydeck = deck()
hand = create_hand(mydeck)
dealer = hand[0]
player = hand[1]

turn_number = 0 # variable used to keep track of how many turns there have been
dealer_Turn = False
play_again = True
ask = False

while play_again == True:
    #
    #gameDisplay.fill(green)
    #card_update()
    dealercount = points(dealer)
    playercount = points(player)
    if turn_number == 0:
        # this is done before you start playing, it will display what cards you have and one of the dealer cards
        print('dealer has')
        print(dealer[0])
        print('you have')
        print(player)
    turn_number += 1

    if playercount == 21 and turn_number == 1: # checks for blackjack only if no turns have gone through
        print('Blackjack! player Wins!')
        break
    elif playercount > 21: # checks if player busts
        print('player busts with:' + str(playercount) + ' points. Dealer wins')
        break
    elif dealer_Turn == True: # only runs after player finishes their turn to avoid dealer from winning too soon
        if dealercount > 21: # check if dealer busts
            print('dealer busts with ' + str(dealer) + ' or ' + str(dealercount) + ' points.')
            print('Player wins with ' + str(player) + ' or ' + str(playercount) + ' points')
            ask = True
            break
        elif dealercount > playercount: # check if dealer has more points than player
            print('Dealer wins with ' + str(dealer) + ' or ' + str(dealercount) + ' points')
            print('Player has:' + str(player) + ' or ' + str(playercount) + ' points')
            ask = True
            break
        elif dealercount < playercount:  # checks if player has more points than dealer
            print('Player wins with ' + str(player) + ' or ' + str(playercount) + ' points')
            print('Dealer has:' + str(dealer) + ' or ' + str(dealercount) + ' points')
            ask = True
            break

    game = input('Would you like to H: hit, or S: stand?\n')
    response = game.lower()
    if response == 'h':
        player.append(mydeck.pop())
        print('dealer has')
        print(dealer[0])
        print('you have')
        print(player)
    elif response == 's':
        dealer_Turn = True

    if ask == True: # this currently doesnt work. supposed to keep the game alive instead of restarting program every time
        play_again_response = input('Would you like to play again? Y: yes, or N: no\n')
        lowercase_play_again_response = play_again_response.lower()
        if lowercase_play_again_response == 'y':
            play_again = True
            ask = False

        elif lowercase_play_again_response == 'n':
            print('Thanks for playing!')
            play_again = False
            ask = False
            break

# THis is awesome

