#File created by: Landon Zafiropoulo
 
# import libraries
# slow the code down if we need it 
from time import sleep
# randomize numbers
from random import randint 
# a comprehensive game library used for python (how we get graphics)
import pygame as pg
# allows use to manage folders and files in directaries 
import os
# finds where the code is in files on computer (where to look for files such as our rock.png)
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings and we capitalize them becuase they are game settings 
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors (RGB values)
# Tuple are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# makes "choices" = a list which is rock paper and scissors to be later used
choices = ["rock", "paper", "scissors"] 

#function to create text on the window
def draw_text(text, size, color, x, y):
    #type of font the text will use
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)
# this is the computer random choice which it chose rock paper or scissors from list above (line 31)
def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("computer randomly decides" + choice)
    return choice
# initializes pygame
pg.init()
pg.mixer.init()
# opens pygame into a windows that we set the values to
screen = pg.display.set_mode((WIDTH, HEIGHT))
# displayes message on the top of the window 
pg.display.set_caption("rock, paper, scissors")

#creates defition for clock to run screen at 30fps
clock = pg.time.Clock()
# rock_image = pg.image.load dispays the variable into a file to when we want to display it we can
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
# rock_image_rect lets up move the code around 
rock_image_rect = rock_image.get_rect()
#making cpu choice equal to the same picture that user picks
cpu_rock_image_rect = rock_image_rect
#sets rock image which is its starting place to 100 in x cord
rock_image_rect.x = 100

paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
#makes the cpu image eqaul to the image that user uses
cpu_paper_image_rect = paper_image_rect
# sets paper image to a x cord
paper_image_rect.x = 350

scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
cpu_scissors_image_rect = scissors_image_rect
scissors_image_rect.x = 550

#storing image for later use when the user interacts
player_image = pg.image.load(os.path.join(game_folder, 'player.jpg')).convert()
player_image_rect = player_image.get_rect()

computer_image = pg.image.load(os.path.join(game_folder, 'computer.jpg')).convert()
computer_image_rect = computer_image.get_rect()

# runs the window until user presses x on screen or esc or alt f4
running = True
#player choice in game
player_choice = ""
#cpu choice in game
cpu_choice = ""
#game runs until shut off (while loop)
while running:
    clock.tick(FPS)

    for event in pg.event.get():
         # when exited window it will stop the loop from running
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONUP:
            # gets mouse cords and the postion of the mouse on screen
            mouse_coords = pg.mouse.get_pos()
            #tracks user mouse waiting util user click on rock
            if rock_image_rect.collidepoint(mouse_coords):
                player_choice = "rock"
                #if user clicked on rock cpu will randomly generate between rock paper or scissors 
                cpu_choice = cpu_randchoice()
                #if user click on paper it will call cpu to randomly generate
            elif paper_image_rect.collidepoint(mouse_coords):
                player_choice = "paper"  
                 #if user clicked on paper cpu will randomly generate between rock paper or scissors 
                cpu_choice = cpu_randchoice()     
            #if clicked on scissor will call cpu to generate
            elif scissors_image_rect.collidepoint(mouse_coords):
                player_choice = "scissors"  
                 #if user clicked on paper cpu will randomly generate between rock paper or scissors 
                cpu_choice = cpu_randchoice()     

                
                
    ########## input ###########
    # HCI = human computer interaction
    # keyboard, mouse, controller, vr headset, touch screen
    
    ########## update ###################
    #move the images by one in x and y cord
    # rock_image_rect.x += 1
    # rock_image_rect.y += 1


    ############ draw ###################
    screen.fill(BLACK)

   # blit means print 
    if player_choice == "":
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, rock_image_rect)
    
    ############# paper ################
    if player_choice == "paper" and cpu_choice == "paper":
        screen.blit(paper_image, paper_image_rect)
        cpu_paper_image_rect.x = 150
        cpu_paper_image_rect.y = 150
        # displays cpu choice (paper)
        screen.blit(paper_image, cpu_paper_image_rect)
        #moves cpu choice to x, y cords
        cpu_paper_image_rect.x = 450
        cpu_paper_image_rect.y = 150
        #draws player image
        screen.blit(player_image,player_image_rect)
        screen.blit(computer_image, computer_image_rect)
        #displays the text onto the screen if called
        draw_text("YOU TIED", 22, BLUE, WIDTH/2, HEIGHT/10)
        #when player choses paper it will move the other pictures of the screen
        if player_choice == "paper":
            rock_image_rect.x = 5000
            scissors_image_rect.x = 5000
            #moves player image after user input
        if player_choice == "paper":
            player_image_rect.x = 150
            player_image_rect.y = 50
           #moves computer_image_rect over after user input
        if player_choice == "paper":
            computer_image_rect.x = 480
            computer_image_rect.y = 50
        
    if player_choice == "paper" and cpu_choice == "scissors":
        screen.blit(paper_image, paper_image_rect)
        cpu_paper_image_rect.x = 150
        cpu_paper_image_rect.y = 150
        # screen.blit(paper_image, paper_image_rect)
        screen.blit(scissors_image, cpu_scissors_image_rect)
        cpu_scissors_image_rect.x = 450
        cpu_scissors_image_rect.y = 150
        screen.blit(player_image,player_image_rect)
        screen.blit(computer_image, computer_image_rect)
        #displays the text onto the screen if called
        draw_text("YOU LOSE", 22, RED, WIDTH/2, HEIGHT/10)
        if player_choice == "paper":
            player_image_rect.x = 150
            player_image_rect.y = 50
        if player_choice == "paper":
            computer_image_rect.x = 480
            computer_image_rect.y = 50

    if player_choice == "paper" and cpu_choice == "rock":
        screen.blit(paper_image, paper_image_rect)
        cpu_paper_image_rect.x = 150
        cpu_paper_image_rect.y = 150
        # screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, cpu_rock_image_rect)
        cpu_rock_image_rect.x = 450
        cpu_rock_image_rect.y = 150
        screen.blit(player_image,player_image_rect)
        screen.blit(computer_image, computer_image_rect)
        #displays the text onto the screen if called
        draw_text("YOU WIN", 22, GREEN, WIDTH/2, HEIGHT/10)
        if player_choice == "paper":
            player_image_rect.x = 150
            player_image_rect.y = 50
        if player_choice == "paper":
            computer_image_rect.x = 480
            computer_image_rect.y = 50
            
    ############# scissors ##############
    if player_choice == "scissors" and cpu_choice == "scissors":
        screen.blit(scissors_image, scissors_image_rect)
        scissors_image_rect.x = 150
        scissors_image_rect.y = 150
        # screen.blit(scissors_image, scissors_image_rect)
        screen.blit(scissors_image, cpu_scissors_image_rect)
        cpu_scissors_image_rect.x = 500
        cpu_scissors_image_rect.y = 150
        #draws image after user input
        screen.blit(player_image,player_image_rect)
        #draws computer image after user input
        screen.blit(computer_image, computer_image_rect)
        #displays the text onto the screen if called
        draw_text("YOU TIED", 22, BLUE, WIDTH/2, HEIGHT/10)
        #when player choses scissors it will move the other images off the screen
        if player_choice == "scissors":
            paper_image_rect.x = 5000
            rock_image_rect.x = 5000
            cpu_paper_image_rect.x = 5000
            cpu_rock_image_rect.x = 5000
            #moves player image after user input
        if player_choice == "scissors":
            player_image_rect.x = 150
            player_image_rect.y = 50
            #moves computer image after called
        if player_choice == "scissors":
            computer_image_rect.x = 480
            computer_image_rect.y = 50

    if player_choice == "scissors" and cpu_choice == "paper":
        screen.blit(scissors_image, scissors_image_rect)
        scissors_image_rect.x = 150
        scissors_image_rect.y = 150
        # screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, cpu_paper_image_rect)
        cpu_paper_image_rect.x = 500
        cpu_paper_image_rect.y = 150
        screen.blit(player_image,player_image_rect)
        screen.blit(computer_image, computer_image_rect)
        #displays the text onto the screen if called
        draw_text("YOU WIN", 22, GREEN, WIDTH/2, HEIGHT/10)
         #moves computer image after called
        if player_choice == "scissors":
            computer_image_rect.x = 480
            computer_image_rect.y = 50

    if player_choice == "scissors" and cpu_choice == "rock":
        screen.blit(scissors_image, scissors_image_rect)
        scissors_image_rect.x = 150
        scissors_image_rect.y = 150
        #displays cpu choice image 
        screen.blit(rock_image, cpu_rock_image_rect)
        #sets cpu image to x, y cords 
        cpu_rock_image_rect.x = 500
        cpu_rock_image_rect.y = 150
        screen.blit(player_image,player_image_rect)
        screen.blit(computer_image, computer_image_rect)
        #displays the text onto the screen if called
        draw_text("YOU WIN", 22, GREEN, WIDTH/2, HEIGHT/10)
         #moves computer image after called
        if player_choice == "scissors":
            computer_image_rect.x = 480
            computer_image_rect.y = 50
################# rock #################
    if player_choice == "rock" and cpu_choice == "rock":
        #displays player choice image
        screen.blit(rock_image, rock_image_rect)
        #moves player choice image torwards specific x, y cords
        rock_image_rect.x = 150
        rock_image_rect.y = 150
        #displays cpu image which is rock 
        screen.blit(rock_image, cpu_rock_image_rect)
        #moves cpu image to specific x, y cords
        cpu_rock_image_rect.x = 500
        cpu_rock_image_rect.y = 150
        #draw player image 
        screen.blit(player_image,player_image_rect)
        #draws computer image
        screen.blit(computer_image, computer_image_rect)
        #displays the text onto the screen if called in color blue
        draw_text("YOU TIED", 22, BLUE, WIDTH/2, HEIGHT/10)
        #when player chooses rock it will move other images off the screen
        if player_choice == "rock":
            paper_image_rect.x = 5000
            scissors_image_rect.x = 5000
            #moves player image after user input
        if player_choice == "rock":
            player_image_rect.x = 150
            player_image_rect.y = 50
        if player_choice == "rock":
            computer_image_rect.x = 480
            computer_image_rect.y = 50

    if player_choice == "rock" and cpu_choice == "paper":
        screen.blit(rock_image, rock_image_rect)
        rock_image_rect.x = 150
        rock_image_rect.y = 150
        # screen.blit(rock_image, rock_image_rect)
        screen.blit(paper_image, cpu_paper_image_rect)
        #moves the cpu image paper to x , y cords
        cpu_paper_image_rect.x = 500
        cpu_paper_image_rect.y = 150
        #drws player image 
        screen.blit(player_image,player_image_rect)
        screen.blit(computer_image, computer_image_rect)
        #displays the text onto the screen if called in color red
        draw_text("YOU LOSE", 22, RED, WIDTH/2, HEIGHT/10)
        if player_choice == "rock":
            player_image_rect.x = 150
            player_image_rect.y = 50
             #moves computer image over after user input
        if player_choice == "rock":
            computer_image_rect.x = 480
            computer_image_rect.y = 50
    #if statment that if player choses rock and cpu choses scissors it calles the images to be put next to eachother
    if player_choice == "rock" and cpu_choice == "scissors":
        #displays rock image
        screen.blit(rock_image, rock_image_rect)
        #moves rock image to new place
        rock_image_rect.x = 150
        rock_image_rect.y = 150
        # displays cpu image of scissors
        screen.blit(scissors_image, cpu_scissors_image_rect)
        #moves cpu image (scissors) to x, y cords
        cpu_scissors_image_rect.x = 500
        cpu_scissors_image_rect.y = 150
        #draws player image
        screen.blit(player_image,player_image_rect)
        screen.blit(computer_image, computer_image_rect)
        #displays the text onto the screen if called in color green
        draw_text("YOU WIN", 22, GREEN, WIDTH/2, HEIGHT/10)
        if player_choice == "rock":
            player_image_rect.x = 150
            player_image_rect.y = 50
        if player_choice == "rock":
            computer_image_rect.x = 480
            computer_image_rect.y = 50

    pg.display.flip()

pg.quit()
