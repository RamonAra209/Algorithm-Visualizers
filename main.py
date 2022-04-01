import os
import pygame
import help_functions as hf

test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pygame.init()
pygame.font.init()
WIN_WIDTH = 1280
WIN_HEIGHT = 720

background_color = [255, 255, 255]
BLACK = [0, 0, 0]
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) # (width, height)

pygame.display.set_caption("That's not a bug, its a feature")

running = True
clock = pygame.time.Clock()
while running:    
    clock.tick(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill(background_color)
    
    rects_dict = hf.create_rects_on_list(test_arr, WIN_WIDTH, WIN_HEIGHT)
    hf.add_recs_to_screen(window, rects_dict)
    
    pygame.display.flip() #* Updates window contents, keep at bottom
    