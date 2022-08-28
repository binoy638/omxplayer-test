import pygame
import os
os.environ["DISPLAY"] = ":0"
pygame.display.init()

# Set up the drawing window
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.NOFRAME)

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                running = False

pygame.quit()