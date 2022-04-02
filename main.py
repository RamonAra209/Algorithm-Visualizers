import os
import time
import pygame
import help_functions as hf
import constants as c
import random
from Brute_Force_Algorithms import bubble_sort  

test_arr = list(range(1, 7))
random.shuffle(test_arr)

pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
window = pygame.display.set_mode((c.WIN_WIDTH, c.WIN_HEIGHT)) # (width, height)

pygame.display.set_caption("That's not a bug, its a feature")

running = True
clock = pygame.time.Clock()
# rects_dict = hf.create_rects_on_list(test_arr, c.WIN_WIDTH, c.WIN_HEIGHT)

while running:    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # window.fill(c.BACKGROUND_COLOR)
    
    # hf.add_recs_to_screen(window, rects_dict)
    # rects_dict = hf.update_rects_positions(rects_dict)    
    # rects_dict = hf.swap_indices(window, rects_dict, 1, 5)
    running = bubble_sort.graphic_bubble_sort(window, test_arr)
    if running == False:
        time.sleep(3)
    pygame.display.flip() #* Updates window contents, keep at bottom
    # pygame.display.update()
   
   
   
   
   
    