import pygame, time, random
from Brute_Force_Algorithms.closest_pair import *
from Brute_Force_Algorithms.selection_sort import graphic_selection_sort, selection_sort
from Divide_and_Conquer.Binary_Tree_Sort.bts import binary_tree_sort 
import help_functions as hf
import constants as c
from Brute_Force_Algorithms import bubble_sort  
from Divide_and_Conquer import *

test_arr = list(range(1, 7))
random.shuffle(test_arr)

pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
window = pygame.display.set_mode((c.WIN_WIDTH, c.WIN_HEIGHT)) # (width, height)

pygame.display.set_caption("That's not a bug, its a feature")

running = True
clock = pygame.time.Clock()
algorithm_choice = hf.print_console_menu() 
print(f"Algorithm Choice = {algorithm_choice}")

if algorithm_choice != 4:
    pygame.display.toggle_fullscreen()
while running:    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if algorithm_choice == 1:
        running = bubble_sort.graphic_bubble_sort(window, test_arr)
    elif algorithm_choice == 2:
        running = graphic_selection_sort(window, test_arr)
    elif algorithm_choice == 3:
        running = graphic_closest_pair(window)
    elif algorithm_choice == 4:
        pygame.display.quit()
        running = binary_tree_sort()
    if running == False:
        time.sleep(3)
    if algorithm_choice != 4:
        pygame.display.flip() #* Updates window contents, keep at bottom

    
