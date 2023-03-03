#File created by: Landon Zafiropoulo
# 
 
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
# initializes pygame
pg.init()
pg.mixer.init()
# opens pygame into a windows that we set the values to
screen = pg.display.set_mode((WIDTH, HEIGHT))
# displayes message on the top of the window 
pg.display.set_caption("Rock, Paper, Scissors...")
#
clock = pg.time.Clock()
# rock_image = pg.image.load dispays the variable into a file to when we want to display it we can
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
# rock_image_rect lets up move the code around 
rock_image_rect = rock_image.get_rect()
rock_image_rect.x = 100

paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
paper_image_rect.x = 350

scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.x = 550
'''
restart_image = pg.image.load(os.path.join(game_folder, 'restart.jpg')).convert()
restart_image_rect = restart_image.get_rect()
restart_image_rect.x = 300
restart_image_rect.y = 300
'''
#storing image for later use when the user wins
youwin_image = pg.image.load(os.path.join(game_folder, 'youwin.jpg')).convert()
youwin_image_rect = youwin_image.get_rect()




running = True

player_choice = ""
cpu_choice = "rock"

while running:
    clock.tick(FPS)

    for event in pg.event.get():
         # when exited window it will stop the loop from running
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONUP:
            # 
            mouse_coords = pg.mouse.get_pos()

            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                player_choice = "rock"
            elif paper_image_rect.collidepoint(mouse_coords):
                player_choice = "paper"       
            elif scissors_image_rect.collidepoint(mouse_coords):
                player_choice = "scissors"       

                
                
    ########## input ###########
    # HCI - human computer interaction...
    # keyboard, mouse, controller, vr headset
    
    ########## update ###################
    # rock_image_rect.x += 1
    # rock_image_rect.y += 1


    ############ draw ###################
    screen.fill(BLACK)

   # blit means print 
    if player_choice == "":
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, rock_image_rect)
    
    if player_choice == "rock":
        screen.blit(rock_image, rock_image_rect)
        #moves image from the starting point to a new point after being clicked on
        rock_image_rect.x = 150
        rock_image_rect.y = 150
    
    
    if player_choice == "paper" and cpu_choice == "rock":
        screen.blit(paper_image, paper_image_rect)
        paper_image_rect.x = 150
        paper_image_rect.y = 100
        screen.blit(rock_image, rock_image_rect)
        rock_image_rect.x = 450
        rock_image_rect.y = 150
        screen.blit(youwin_image, youwin_image_rect)
        youwin_image_rect.x = 250
        youwin_image_rect.y = 400
    
    if player_choice == "scissors":
        screen.blit(scissors_image, scissors_image_rect)
        scissors_image_rect.x = 150
        scissors_image_rect.y = 150


    # if cpu_choice == "rock":
    #        screen.blit(rock_image, rock_image_rect)


    pg.display.flip()

pg.quit()
