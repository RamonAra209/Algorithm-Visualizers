import os
import time
import pygame
from Brute_Force_Algorithms.closest_pair import *
from Brute_Force_Algorithms.selection_sort import graphic_selection_sort, selection_sort 
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
    # running = bubble_sort.graphic_bubble_sort(window, test_arr)
    # running = graphic_selection_sort(window, test_arr)
    points = [5, 1] #! Delete this, just a palceholder
    running = graphic_closest_pair(window, points)
    if running == False:
        time.sleep(3)
    pygame.display.flip() #* Updates window contents, keep at bottom
    # pygame.display.update()