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




# deck should be defined first outside of any loop for now.  Game should continue to pop off of the top of the deck until the deck is almost gone

def deck():
    # deck joins the suits and ranks of a deck and then shuffles the deck into a random order
    deck = []
    for suit in ['H', 'S', 'C', 'D']:
        for rank in ['A', 'J', 'Q', 'K', 'T', '9', '8', '7', '6', '5', '4', '3', '2']:
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
def pointsforaces(mycards):
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

    if ace_count != 0:
        while ace_count != 0:
            my_points += 1

            if my_points <= 11 and ace_count == 1:
                my_points +=10
            ace_count -= 1


    return int(my_points)

def Dealer_Ace_Check(mycards):
    # Function Checks the dealers top card to see if its an Ace so insurance can be offered


    if mycards[0] == 'CA' or mycards[0] == 'SA' or mycards[0] == 'DA' or mycards[0] == 'HA':
        ace_top = 1
    else:
        ace_top = 0

    return int(ace_top)

def create_dealer_hand(mydeck):
    # the create hand function will take in an argument called my deck
    # this function creates two hands my_hand and dealer_hand and returns them
    # my_hand will give you two cards
    # the dealer_hand will be created and made fully but not shown
    dealer_hand = []
    dealer_hand.append(mydeck.pop())
    dealer_hand.append(mydeck.pop())



    return [dealer_hand]
def create_player_hand(mydeck):
    # the create hand function will take in an argument called my deck
    # this function creates two hands my_hand and dealer_hand and returns them
    # my_hand will give you two cards
    # the dealer_hand will be created and made fully but not shown
    my_hand = []
    my_hand.append(mydeck.pop())
    my_hand.append(mydeck.pop())



    return [my_hand]
def get_player_bet_amount():
    bet_amount = 0
    while bet_amount <= 0:
        try:
            bet_amount = float(input('How much would you like to bet?\n'))
            if bet_amount <= player_money and bet_amount >=1 :
                break
            else:
                print('You don\'t have that much money' )
                bet_amount = 0

        except ValueError:
            print('Please input a number')

    return bet_amount
def check_for_spilt(hand,bet,money,hands):
    ace = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    for i in hand:
            if i[1] == 'J' or i[1] == 'Q' or i[1] == 'K' or i[1] == 'T':
                ten += 1
            elif i[1] == 'A':
                ace += 1
            elif i[1] == '2':
                two += 1
            elif i[1] == '3':
                three += 1
            elif i[1] == '4':
                four += 1
            elif i[1] == '5':
                five += 1
            elif i[1] == '6':
                six += 1
            elif i[1] == '7':
                seven += 1
            elif i[1] == '8':
                eight += 1
            elif i[1] == '9':
                nine += 1
    if ace == 2 or two == 2 or three == 2 or four == 2 or five == 2 or six == 2 or seven == 2 or eight == 2 or nine == 2 or ten == 2:
        if money >= bet and hands < 4:
            can_spilt = True
        else:
            can_spilt = False
    else:
        can_spilt = False


    return can_spilt
def spilt(poss_spilt,hand,hand_final,num_hands,num_spilts):



    return hands
mydeck = deck()
turn_number = 0 # variable used to keep track of how many turns there have been
play_again = True
player_money = 100.0
shuffle_again = True

while shuffle_again == True:
    print('You have $',player_money)
    dealer_Turn = False
    play_again = True
    ask = False
    while play_again == True:
        while play_again == True:

# betting phase before gameplay starts
            bet = get_player_bet_amount()
            print('Player has bet $',bet)
            player_money_left = player_money - bet
            print('You now have $' + str(player_money_left))

            game = ''
            insurance = ''
            #player_hand = create_player_hand(mydeck)
            #player = player_hand[0]
            #dealer_hand = create_dealer_hand(mydeck)
            #dealer = dealer_hand[0]
            number_of_splits = 0
            number_of_hands = 1
            dealer = []
            hands_values = []
            hands = []
            hands_final = []
            doubles_flag = []
            player = []
            player.append(mydeck.pop())
            dealer.append(mydeck.pop())
            player.append(mydeck.pop())
            dealer.append(mydeck.pop())
            hands = [player]
            dealer_draw_cards = False

            #
            #gameDisplay.fill(green)
            #card_update()
            dealercount = pointsforaces(dealer)
            playercount = pointsforaces(player)

            dealerTopcardCount = Dealer_Ace_Check(dealer)
# this is done before you start playing, it will display what cards you have and one of the dealer cards
            print('dealer has')
            print(dealer[0])
            print('you have')
            print(player,playercount)
# check for spilt possibility
            possible_spilt = False
            possible_spilt = check_for_spilt(player,bet,player_money_left,number_of_hands)



            if dealercount == 21 and dealerTopcardCount == 0 and playercount != 21:
                player_money -= bet
                print('Dealer has non Ace showing 21')
                ask = True
                break
# player gets blackjack and dealer is showing an ace

            elif playercount == 21 and dealerTopcardCount == 1: # checks for blackjack only if no turns have gone through
                even_money = input('Would you like even money? Y for Yes, N for No\n')
                response = even_money.lower()
                if response == 'y':
                    player_money += (bet)
                    print('You took even money.')
                    print('You now have $',player_money)
                    print('Dealer had ' + str(dealer))
                    ask = True
                    break
                if response == 'n' and dealercount == 21:
                    print('Dealer also has 21, its a push!')
                    print('You now have $', player_money)
                    ask = True
                    break
                if response == 'n' and dealercount != 21:
                    print('dealer does not have 21, you win!')
                    player_money += (bet*1.5)
                    print('You now have $', player_money)
                    ask = True
                    break
            elif playercount == 21: # checks for blackjack only if no turns have gone through
                print('Blackjack! player Wins!')
                player_money += (bet*1.5)
                print('You now have $', player_money)
                ask = True
                break
# dealer shows an ace
            elif dealerTopcardCount ==  1:
                insurance = input('Would you like to buy Insurance? Y for Yes, N for No\n')
                response = insurance.lower()
                if response == 'y' and dealercount == 21 and bet/2 > player_money_left:
                    print ('You cant afford insurance silly, and the Dealer has 21,you lose!\n')
                    player_money -= bet
                    print('You now have $', player_money)
                    ask = True
                    break
                elif response == 'y' and dealercount != 21 and bet/2 > player_money_left:
                    print ('You cant afford insurance silly!\n')
                elif response == 'y' and dealercount == 21 and bet/2 <= player_money_left:
                    print ('Dealer has 21, keep your money!\n')
                    print('You now have $', player_money)
                    ask = True
                    break
                elif response == 'y' and dealercount != 21 and bet/2 <= player_money_left:
                    print('Dealer does not have 21, you lose your insurance money:',(bet/2),'\n')
                    player_money -= (bet/2)
                elif response != 'y' and dealercount == 21:
                    print('Dealer has 21, you lose\n')
                    player_money -= bet
                    print('You now have $', player_money)
                    ask = True
                    break
                elif response != 'y' and dealercount != 21:
                    print('Dealer does not have 21, continue playing\n')

# checks to see if spilt is an option



# if there are no blackjacks or dealer 21s (regular game) Flaggggggggggggggggggggjgjgjgjgjgjgjgjgjgjjgjgjgjgjgjjgjgjgjgjgjggjjgjgjg
            hit_counter = 0
            while dealer_Turn == False:
                hand_turn = True
                dealer_Turn = False
                for x in hands:

                    hand_turn = True
                    hit_counter = 0
                    did_spilt = False

                    while hand_turn == True:



                        possible_spilt = check_for_spilt(x, bet, player_money_left, number_of_hands)
                        if number_of_hands > 1:
                            print('You have', hands)
                            print('The hand you are playing is: ',x)
                            if len(hands_final) >= 1:
                                if x == hands_final[0]:
                                    print(x)
                                    break
                            if len(hands_final) == 2:
                                if x == hands_final[1]:
                                    print(x)
                                    break
                        if possible_spilt == True:
                            game = input('Would you like to H: hit,or D: double, or S: stand, or P: Split?\n')
                            response = game.lower()
                        else:
                            game = input('Would you like to H: hit,or D: double, or S: stand?\n')
                            response = game.lower()
        # spilt
                        if response == 'p' and possible_spilt == True:
                            number_of_hands += 1
                            number_of_splits += 1
                            dealer_Turn = False
                            if number_of_splits == 1:
                                hands = x[::2],x[1::2]
                                player_money_left -= bet
                                did_spilt = True
                                break
                            if number_of_splits == 2 and len(hands_final) == 1:
                                hands = hands_final[0],x[::2],x[1::2]
                                player_money_left -= bet
                                did_spilt = True
                                break
                            if number_of_splits == 2:
                                hands_temp = hands[1]
                                hands = x[::2],x[1::2],hands_temp
                                player_money_left -= bet
                                did_spilt = True
                                break
                            if number_of_splits == 3 and len(hands_final)==0:
                                hands_temp1 = hands[1]
                                hands_temp2 = hands[2]
                                hands = x[::2],x[1::2],hands_temp1,hands_temp2
                                player_money_left -= bet
                                did_spilt = True
                                break
                            if number_of_splits == 3 and len(hands_final)==1:
                                hands_temp = hands[2]
                                hands = hands_final[0],x[::2],x[1::2],hands_temp
                                player_money_left -= bet
                                did_spilt = True
                                break
                            if number_of_splits == 3 and len(hands_final)==2:
                                hands = hands_final[0],hands_final[1],x[::2],x[1::2]
                                player_money_left -= bet
                                did_spilt = True
                                break


                        elif response == 'p' and possible_spilt == False:
                            if number_of_hands < 4:
                                print('You cant spilt those cards, or you dont have enough money!')
                            else:
                                print('You arent allowed to split more than 3 times')
        # hit
                        elif response == 'h':
                                x.append(mydeck.pop())
                                hit_counter += 1
                                playercount = pointsforaces(x)
                                print('dealer has')
                                print(dealer[0])
                                print('you have')
                                print(x,playercount)

                                if(playercount==21):
                                    hand_turn = False
                                    dealer_Turn = True
                                    hands_final.append(x)
                                    doubles_flag.append(1)
                                    print('Nice Hit!')

                                elif(playercount > 21 and number_of_splits >= 1):
                                    hand_turn = False
                                    dealer_Turn = True
                                    hands_final.append(x)
                                    doubles_flag.append(1)
                                    print('You busted that hand.')
                                elif(playercount > 21):
                                    hand_turn = False
                                    dealer_Turn = True
                                    hands_final.append(x)
                                    doubles_flag.append(1)
                                    print('You busted!')



        # double
                        elif response == 'd':
                            if player_money >= bet*2 and len(x) == 2:
                                    doubles_flag.append(2)
                                    bet = bet
                                    player_money_left -= bet
                                    print('Your bet is now',2*bet)
                                    x.append(mydeck.pop())
                                    playercount = pointsforaces(x)
                                    print('dealer has')
                                    print(dealer[0])
                                    print('you have')
                                    print(x, playercount)
                                    hands_final.append(x)
                                    hand_turn = False
                                    dealer_Turn = True

                            elif hit_counter > 0 or len(x) !=2:
                                print('You can only double on the first card!')
                            else:
                                print('You dont have enough money to double!')

        #stay
                        else:
                            hands_final.append(x)
                            doubles_flag.append(1)
                            hand_turn = False
                            dealer_Turn = True



                    hand_turn = False
                    if did_spilt == True:
                        break


            dealer_Turn = False
# checks if player busts
            if number_of_hands > 1:
                print(hands_final)
            for y in hands_final:
                if pointsforaces(y) <= 21:
                    dealer_draw_cards = True
                    break
                else:
                    dealer_draw_cards = False
# if the dealer has less than 16 and the player hasnt busted the dealer will hit until he gets 17 or busts
            if dealer_draw_cards == True:
                    while dealercount <= 16:
                        dealer.append(mydeck.pop())
                        dealercount = pointsforaces(dealer)
            for z in hands_final:
                reset_bet = False

                playercounts = pointsforaces(z)
                if z == hands_final[0]:
                    bet = bet*doubles_flag[0]
                    if doubles_flag[0] == 2:
                        reset_bet = True
                elif z == hands_final[1]:
                    bet = bet*doubles_flag[1]
                    if doubles_flag[1] == 2:
                        reset_bet = True
                elif z == hands_final[2]:
                    bet = bet*doubles_flag[2]
                    if doubles_flag[2] == 2:
                        reset_bet = True
                elif z == hands_final[3]:
                    bet = bet*doubles_flag[3]
                    if doubles_flag[3] == 2:
                        reset_bet = True

                if playercounts > 21:
                        print('player busts with:' + str(playercounts) + ' points. Dealer wins')
                        print('Dealer had ' + str(dealer))
                        player_money -= bet
                        ask = True

                elif dealercount > 21: # check if dealer busts
                        print('dealer busts with ' + str(dealer) + ' or ' + str(dealercount) + ' points.')
                        print('Player wins with ' + str(z) + ' or ' + str(playercounts) + ' points')
                        player_money += bet
                        ask = True

                elif dealercount > playercounts: # check if dealer has more points than player
                        print('Dealer wins with ' + str(dealer) + ' or ' + str(dealercount) + ' points')
                        print('Player has:' + str(z) + ' or ' + str(playercounts) + ' points')
                        player_money -= bet
                        ask = True

                elif dealercount < playercounts:  # checks if player has more points than dealer
                        print('Player wins with ' + str(z) + ' or ' + str(playercounts) + ' points')
                        print('Dealer has:' + str(dealer) + ' or ' + str(dealercount) + ' points')
                        player_money += bet
                        ask = True

                elif dealercount == playercounts:  # checks if there is a tie
                        print('Its a push with ' + str(z) + ' or ' + str(playercounts) + ' points')
                        print('Dealer had:' + str(dealer) + ' or ' + str(dealercount) + ' points')
                        ask = True
                else:
                    ask = True
                if reset_bet == True:
                    bet = bet/2

                print('You now have $' + str(player_money))
                player_money_left = player_money
            break

        # keeps the game alive instead of restarting program every time\
        if ask == True and len(mydeck) > 9:
                    play_again_response = input('Would you like to play again? Y: yes, or N: no\n')
                    lowercase_play_again_response = play_again_response.lower()
                    if lowercase_play_again_response == 'y' and player_money >=1:
                        play_again = True
                    elif lowercase_play_again_response == 'y' and player_money < 1:
                        buy_back_response = input('You are out of money! Would you like to buy back in? Y: yes, or N: no\n')
                        lowercase_buy_back_response = buy_back_response.lower()
                        if buy_back_response == 'y':
                            player_money = 100.0
                            play_again = True
                        else:
                            play_again = False
                            shuffle_again = False
                            ask = False
                    elif lowercase_play_again_response != 'y':
                        print('Thanks for playing!')
                        play_again = False
                        shuffle_again = False
                        ask = False
        # when deck gets to low to play another hand it will ask to reshuffle
        elif ask == True and len(mydeck) <= 9:
                if player_money >= 1:
                    shuffle_again_response = input('Would you like to reshuffle and play again? Y: yes, or N: no\n')
                    lowercase_shuffle_again_response = shuffle_again_response.lower()
                    if lowercase_shuffle_again_response == 'y':
                        shuffle_again = True
                        mydeck = deck()

                    elif lowercase_shuffle_again_response != 'y':
                        print('Thanks for playing!')
                        shuffle_again = False
                        ask = False
        else:
                    shuffle_again_response = input('Would you like to reshuffle, buy back in, and play again? Y: yes, or N: no\n')
                    lowercase_shuffle_again_response = shuffle_again_response.lower()
                    if lowercase_shuffle_again_response == 'y':
                        shuffle_again = True
                        mydeck = deck()
                        player_money = 100.0
                    elif lowercase_shuffle_again_response != 'y':
                        print('Thanks for playing!')
                        shuffle_again = False
                        ask = False



            # This is awesome

