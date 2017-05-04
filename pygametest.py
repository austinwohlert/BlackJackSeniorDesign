import pygame

pygame.init()

display_width = 800   # creates a variable for width of screen
display_height = 600  # creates a variable for height of screen

gameDisplay = pygame.display.set_mode((display_height, display_width))  # creates a variable for game display with#  the height and width
pygame.display.set_caption('A pygame Test')  # this will label the pop up window with something inside the string

# creating colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)
two_of_clubs = pygame.image.load('/Users/Austin/PycharmProjects/BlackJack/cards/2_of_clubs.png') # cardimg will load the 2 of clubs
two_of_clubs = pygame.transform.scale(two_of_clubs, (100,200))
three_of_clubs = pygame.transform.scale(pygame.image.load('/Users/Austin/PycharmProjects/BlackJack/cards/3_of_clubs.png'), (100,200))

def card(x,y,):
    gameDisplay.blit(two_of_clubs, (x, y))
    gameDisplay.blit(three_of_clubs, (x + 50, y + 50))
y_change = 0
x_change = 0
x = (display_width * .45)
y = (display_height * .8)
play = True
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 0
    x += x_change
    y += y_change
    gameDisplay.fill(green)
    card(x, y)
    pygame.display.update()

pygame.quit()
quit()

