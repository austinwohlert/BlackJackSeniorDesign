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
import sys

display_width = 1000
display_height = 1500
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
blue = (0,0,255)
green = (0, 250, 0)
# deck should be defined first outside of any loop for now.  Game should continue to pop off of the top of the deck until the deck is almost gone

def deck():
    # deck joins the suits and ranks of a deck and then shuffles the deck into a random order
    deck = []
    for suit in ['H', 'S', 'C', 'D']:
        for rank in ['A', 'J', 'Q', 'K', 'T', 'T', 'T', 'T', 'T', '7', '8', '9', 'T']:
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
            if my_points <= 11:
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
def check_for_spilt(hand,bet,money):
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
    if ace >= 2 or two >= 2 or three >= 2 or four >= 2 or five >= 2 or six >= 2 or seven >= 2 or eight >= 2 or nine >= 2 or ten >= 2:
        if money >= bet:
            can_spilt = True
        else:
            can_spilt = False
    else:
        can_spilt = False

    return can_spilt
def spilt(hand):
    return hand[::2],hand[1::2]



def player_info_box(players_bet, players_money):
    xpos1 = 30
    ypos1 = 40
    myFont = pygame.font.SysFont('Verdana.ttf', 28)
    pygame.draw.rect(gameDisplay, green, (xpos1, ypos1 - 10, xpos1 + 150, ypos1 + 1))
    pygame.draw.rect(gameDisplay, green, (xpos1, ypos1+22, xpos1 + 150, ypos1 + 1))
    pygame.display.update()
    players_bet_to_screen = myFont.render(str('Your Bet:'), 1, black)
    players_inputbet_to_screen = myFont.render(str(players_bet), 1, black)
    players_money_to_screen = myFont.render(str('You have:'), 1, black)
    players_inputmoney_to_screen = myFont.render(str(players_money), 1, black)
    gameDisplay.blit(players_money_to_screen,(xpos1,ypos1))
    gameDisplay.blit(players_inputmoney_to_screen, (xpos1+110, ypos1))
    gameDisplay.blit(players_bet_to_screen,(30,62)) # 30,62
    gameDisplay.blit(players_inputbet_to_screen, (140, 62)) #140,62
    pygame.display.update()

#might need to make this all one big draw buttons function but need to add functionality to buttons

def hit_button():

    pygame.draw.rect(gameDisplay, red, (200, 850, 125, 100))
    pygame.display.update()

def stand_button():

    pygame.draw.rect(gameDisplay, red, (444, 850, 125, 100))
    pygame.display.update()

def split_button():

    pygame.draw.rect(gameDisplay, red, (688, 850, 125, 100))
    pygame.display.update()

def double_button():

    pygame.draw.rect(gameDisplay, red, (932, 850, 125, 100))
    pygame.display.update()

def surrender_button():

    pygame.draw.rect(gameDisplay, red, (1176, 850, 125, 100))
    pygame.display.update()

def get_key_press():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            print('h')
            return 'h'

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            return 's'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            return 'd'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
            return 'y'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            return 'n'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            return 'p'
        else:
            pygame.time.wait(20)
    pygame.display.flip()
    pygame.time.wait(20)


mydeck = deck()
turn_number = 0 # variable used to keep track of how many turns there have been
play_again = True
player_money = 100.0
shuffle_again = True




pygame.init()
gameDisplay = pygame.display.set_mode((display_height,display_width), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption('BlackJack')
gameDisplay.fill(green)
pygame.display.update()
bet = 0
player_info_box(bet, player_money)
hit_button()
stand_button()
split_button()
double_button()
surrender_button()


while shuffle_again is True:

        player_info_box(bet, player_money)
        print('You have $',player_money)
        dealer_Turn = False
        play_again = True
        ask = False
        while play_again is True:
            for event in pygame.event.get():
                #else:
                #    pygame.time.wait(20)


                    # betting phase before gameplay starts
                bet = get_player_bet_amount()
                print('Player has bet $',bet)
                player_money_left = player_money - bet
                print('You now have $' + str(player_money_left))
                player_info_box(bet, player_money_left)
                game = ''
                insurance = ''
                player_hand = create_player_hand(mydeck)
                player = player_hand[0]
                dealer_hand = create_dealer_hand(mydeck)
                dealer = dealer_hand[0]
                number_of_hands = 1
                dealercount = pointsforaces(dealer)
                playercount = pointsforaces(player)

                dealerTopcardCount = Dealer_Ace_Check(dealer)
    # this is done before you start playing, it will display what cards you have and one of the dealer cards
                print('dealer has')
                print(dealer[0])
                print('you have')
                print(player, playercount)
    # check for spilt possibility
                possible_spilt = False
                possible_spilt = check_for_spilt(player,bet,player_money_left)



                if dealercount is 21 and dealerTopcardCount is 0 and playercount is not 21:
                    player_money -= bet
                    print('Dealer has non Ace showing 21')
                    break
    # player gets blackjack and dealer is showing an ace

                if playercount == 21 and dealerTopcardCount == 1: # checks for blackjack only if no turns have gone through
                    even_money = input('Would you like even money? Y for Yes, N for No\n')
                    response = even_money.lower()
                    if response == 'y':
                        player_money += (bet)
                        ask = True
                        break
                    if response == 'n' and dealercount == 21:
                        print('Dealer also has 21, its a push!')
                        ask = True
                        break
                    if response == 'n' and dealercount != 21:
                        print('dealer does not have 21, you win!')
                        player_money += (bet*1.5)
                        ask = True
                        break
                if playercount == 21: # checks for blackjack only if no turns have gone through
                    print('Blackjack! player Wins!')
                    player_money += (bet*1.5)
                    ask = True
                    break
    # dealer shows an ace
                if dealerTopcardCount == 1:
                    insurance = input('Would you like to buy Insurance? Y for Yes, N for No\n')
                    response = insurance.lower()
                    if response == 'y' and dealercount == 21 and bet/2 > player_money_left:
                        print ('You cant afford insurance silly, and the Dealer has 21,you lose!\n')
                        player_money -= bet
                        ask = True
                        break
                    if response == 'y' and dealercount != 21 and bet/2 > player_money_left:
                        print ('You cant afford insurance silly!\n')
                    if response == 'y' and dealercount == 21 and bet/2 <= player_money_left:
                        print ('Dealer has 21, keep your money!\n')
                        ask = True
                        break
                    if response == 'y' and dealercount != 21 and bet/2 <= player_money_left:
                        print('Dealer does not have 21, you lose your insurance money:',(bet/2),'\n')
                        player_money -= (bet/2)
                    if response != 'y' and dealercount == 21:
                        print('Dealer has 21, you lose\n')
                        player_money -= bet
                        ask = True
                        break
                    if response != 'y' and dealercount != 21:
                        print('Dealer does not have 21, continue playing\n')

    # checks to see if spilt is an option



    # if there are no blackjacks or dealer 21s (regular game)
                hit_counter = 0


                if possible_spilt == True:
                    game = input('Would you like to H: hit,or D: double, or S: stand, or P: Split?\n')
                    response = game.lower()
                else:
                    game = input('Would you like to H: hit,or D: double, or S: stand?\n')
                    response = game.lower()
# spilt
                if response == 'p' and possible_spilt == True:
                    number_of_hands += 1
                    hand1,hand2 = spilt(player)
                    dealer_Turn = True

                elif response == 'p' and possible_spilt == False:
                    print('You cant spilt those cards, or you dont have enough money!')
# hit
                elif response == 'h':
                    player.append(mydeck.pop())
                    hit_counter += 1
                    playercount = pointsforaces(player)
                    print('dealer has')
                    print(dealer[0])
                    print('you have')
                    print(player,playercount)

                    if(playercount > 21):
                        dealer_Turn = True
# double
                elif response == 'd':
                    if player_money >= bet*2 and hit_counter == 0:
                        bet = bet*2
                        print('Your bet is now',bet)
                        player.append(mydeck.pop())
                        playercount = pointsforaces(player)
                        print('dealer has')
                        print(dealer[0])
                        print('you have')
                        print(player, playercount)
                        dealer_Turn = True
                    elif hit_counter > 0:
                        print('You can only double on the first card!')
                    else:
                        print('You dont have enough money to double!')

#stay
                else:
                    dealer_Turn = True
# spilt situation SPECIAL
                if number_of_hands == 2:
    #clearing things up and resetting them for Hand 1.
                    possible_spilt = False
                    next_Hand = False
                    hand1.append(mydeck.pop())
                    bet1 = bet
                    player_money_left = player_money - bet1
                    check_for_spilt(hand1,bet1,player_money_left)
                    hit_counter1 = 0
                    hand1count = pointsforaces(hand1)
                    print('Hand 1 is',hand1,hand1count)

    #play hand one
                    while next_Hand == False:
                        if possible_spilt == True:
                            game = input('Would you like to H: hit,or D: double, or S: stand, or P: Split?\n')
                            response = game.lower()
                        else:
                            game = input('Would you like to H: hit,or D: double, or S: stand?\n')
                            response = game.lower()
        # spilt
                        if response == 'p' and possible_spilt == True:
                            number_of_hands += 1
                            hand1,hand3 = spilt(hand1)

                        elif response == 'p' and possible_spilt == False:
                            print('You cant spilt those cards, or you dont have enough money!')
        # hit
                        elif response == 'h':
                                hand1.append(mydeck.pop())
                                hand1count = pointsforaces(hand1)
                                hit_counter1 += 1
                                print('you have')
                                print(hand1,hand1count)

                                if(hand1count > 21):
                                    print('You busted, now play next hand.')
                                    next_Hand = True
        # double
                        elif response == 'd':
                            if player_money >= bet1*2 and hit_counter1 == 0:
                                bet1 = bet1*2
                                print('Your bet is now',bet1)
                                hand1.append(mydeck.pop())
                                hand1count = pointsforaces(hand1)
                                print('You have')
                                print(hand1, hand1count)
                                next_Hand = True
                            elif hit_counter > 0:
                                print('You can only double on the first card!')
                            else:
                                print('You dont have enough money to double!')

        #stay
                        else:
                            next_Hand = True


    #play Hand 2
                    print('Hand 1: ',hand1, hand1count,'\nHand 2: ',hand2)
                    break

    # checks if player busts
                if playercount > 21:
                        print('player busts with:' + str(playercount) + ' points. Dealer wins')
                        print('Dealer had ' + str(dealer))
                        player_money -= bet
                        ask = True
                        break
    # if the dealer has less than 16 and the player hasnt busted the dealer will hit until he gets 17 or busts
                while dealercount <= 16:
                    dealer.append(mydeck.pop())
                    dealercount = pointsforaces(dealer)
                if dealercount > 21: # check if dealer busts
                        print('dealer busts with ' + str(dealer) + ' or ' + str(dealercount) + ' points.')
                        print('Player wins with ' + str(player) + ' or ' + str(playercount) + ' points')
                        player_money += bet
                        ask = True
                        break
                if dealercount > playercount: # check if dealer has more points than player
                        print('Dealer wins with ' + str(dealer) + ' or ' + str(dealercount) + ' points')
                        print('Player has:' + str(player) + ' or ' + str(playercount) + ' points')
                        player_money -= bet
                        ask = True
                        break
                if dealercount < playercount:  # checks if player has more points than dealer
                        print('Player wins with ' + str(player) + ' or ' + str(playercount) + ' points')
                        print('Dealer has:' + str(dealer) + ' or ' + str(dealercount) + ' points')
                        player_money += bet
                        ask = True
                        break
                if dealercount == playercount:  # checks if there is a tie
                        print('Its a push with ' + str(player) + ' or ' + str(playercount) + ' points')
                        print('Dealer had:' + str(dealer) + ' or ' + str(dealercount) + ' points')
                        ask = True
                        break
        print('You now have $' + str(player_money))
        player_money_left = player_money
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


