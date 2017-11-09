import pygame
import imghdr
import os

'''

Currently have a function that will go through all the picture files and strip out the card name from each file.
I also have created an image dictionary that has the card paired with the location of the image

need to figure out how to display different images to the screen at will  DONE

need to figure out how to position cards at certain spots on the board

dealer hand position and player hand position

'''
card_width = 100   # width of your playing card
card_height = 200  # height of your playing card
#x_move = 0          # amount in x direction to offset
display_width = 1000 # display size in pixels wide
display_height = 750 # display size in pixels high
#x = (display_width/2 - card_width/2)  #
#y = card_height/3  # not sure
dealer_y = card_height/3  # y position of top left corner of first card
dealer_x = (display_width/2 - card_width/2) # x position of dealer card location
player_y = .666*display_height # y position of player cards
player_x = (display_width/2-(card_width/2)) # x position of player cards
gameDisplay = pygame.display.set_mode((display_width, display_height))  # creates a canvas with certain width and height
pygame.display.set_caption('A pygame Test') # names the created window ' a pygame test'
pygame.init()   # init pygame
directory_dict = []  # list of all directories of where card image is located
card_dict = []   # list of all cards with format 2_"card"
replaced_card_dict = []   # list of all cards with number replaced by spelling two_"card"
green = (0, 128, 0) # green color
size_of_card = (card_width, card_height)  # size of the card x,y
directory_path = '/Users/Austin/PycharmProjects/BlackJack/cards/'
# this is the path where cards are stored. WILL NEED TO BE CHANGED FOR PI''''
# code will need to change because the amount of numbers stripped in the directory will vary depending on the size of the directory
# Austin Mac directory path ----  '/Users/Austin/PycharmProjects/BlackJack/cards/'
# Austin Windows directory path -- '\\Users\\randy\\PycharmProjects\\BlackJackSeniorDesign\\cards\\'
hands = ['D2', 'S4',
         'D5']  # this i just a test hand. will need to replace it in the while loop where it is for hand in hand_to_image(hands)
player_hand = ['D2', 'S4', 'D5']  # test hand for the player
for dirpath, dirnames, filenames in os.walk(directory_path):  # this walks through all card images and makes a dictionary with just the cards name from the file
    # takes the directory_path and each card's path and makes a dictionary of all of the names
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        if imghdr.what(file_path):
            directory_dict.append(file_path)
            new_filepath = file_path.replace('', '')[:-4]
            card_image_name = new_filepath[len(directory_path):]  # should be 46
            card_dict.append(card_image_name)

#print(card_dict)
# 57

for card in card_dict:   # this will replace all numbers in string from the original name of the file with their spelling and add to a dictionary called replaced_card_dict
    #this is done because starting the name of something with a number will cause problems in python
    if card[0:2] == '10':
        new_card = card.replace('10', 'Ten')
        replaced_card_dict.append(new_card)
    elif card[0] == '2':
        new_card = card.replace('2', 'Two')
        replaced_card_dict.append(new_card)
    elif card[0] == '3':
        new_card = card.replace('3', 'Three')
        replaced_card_dict.append(new_card)
    elif card[0] == '4':
        new_card = card.replace('4', 'Four')
        replaced_card_dict.append(new_card)
    elif card[0] == '5':
        new_card = card.replace('5', 'Five')
        replaced_card_dict.append(new_card)
    elif card[0] == '6':
        new_card = card.replace('6', 'Six')
        replaced_card_dict.append(new_card)
    elif card[0] == '7':
        new_card = card.replace('7', 'Seven')
        replaced_card_dict.append(new_card)
    elif card[0] == '8':
        new_card = card.replace('8', 'Eight')
        replaced_card_dict.append(new_card)
    elif card[0] == '9':
        new_card = card.replace('9', 'Nine')
        replaced_card_dict.append(new_card)
    else:
        replaced_card_dict.append(card)

image_dict = dict(zip(replaced_card_dict, directory_dict))

def hand_to_image(hands): # this takes in a list of cards in playing form S4 and returns a string such as four_of_spades that can be read by other function
        card_box = []
        for hand in hands:

            if hand[1] == '2':
                card_string = 'Two_of_'
            elif hand[1] == '3':
                card_string = 'Three_of_'
            elif hand[1] == '4':
                card_string = 'Four_of_'
            elif hand[1] == '5':
                card_string = 'Five_of_'
            elif hand[1] == '6':
                card_string = 'Six_of_'
            elif hand[1] == '7':
                card_string = 'Seven_of_'
            elif hand[1] == '8':
                card_string = 'Eight_of_'
            elif hand[1] == '9':
                card_string = 'Nine_of_'
            elif hand[1] == 'T':
                card_string = 'Ten_of_'
            elif hand[1] == 'J':
                card_string = 'Jack_of_'
            elif hand[1] == 'Q':
                card_string = 'Queen_of_'
            elif hand[1] == 'K':
                card_string = 'King_of_'
            elif hand[1] == 'A':
                card_string = 'Ace_of_'
            if hand[0] == 'H':
                card_string = card_string + 'hearts'
            if hand[0] == 'S':
                card_string = card_string + 'spades'
            if hand[0] == 'C':
                card_string = card_string + 'clubs'
            if hand[0] == 'D':
                card_string = card_string + 'diamonds'
            card_box.append(card_string)
        return card_box
def cards_display(x, y, what_card):
    # this takes in a position x,y and the card you want to display
    # it then scales the image and uses pygame to display this image at a certain place
    display_card = pygame.transform.scale(pygame.image.load(image_dict[what_card]), size_of_card)
    gameDisplay.blit(display_card, (x, y))

game = True

def player_cards_display(x, y, what_card): # displays players cards at players position
    move = 0
    for hand in hand_to_image(what_card):
        cards_display(dealer_x+move, y, hand)
        move += card_width/3
        pygame.display.update()

def dealer_cards_display(x, y, what_card): # displays dealers cards at dealers position
    move = 0
    for hand in hand_to_image(what_card):
        cards_display(dealer_x+move,y, hand)
        move += card_width/3
        pygame.display.update()
def dealer_cards_display_one_card(x, y, what_card): # displays dealers cards at dealers position
    move = 0
    cards_display(dealer_x+move,y, hand_to_image(what_card[0]))
    move += card_width/3
    pygame.display.update()
def card_update(): # combines previous two functions
    player_cards_display(player_x, player_y, player_hand)
    dealer_cards_display(dealer_x, dealer_y, reversed(hands))


while True: # main game loop

    gameDisplay.fill(green)
    card_update()
    pygame.time.wait(10000)
    pygame.quit()
    quit()



