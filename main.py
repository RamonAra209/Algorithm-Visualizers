import pygame, time, random, os
from Brute_Force_Algorithms.closest_pair import *
from Brute_Force_Algorithms.selection_sort import graphic_selection_sort, selection_sort
from Divide_and_Conquer.bts import binary_tree_sort 
import help_functions as hf
import constants as c
from Brute_Force_Algorithms import bubble_sort  
from Divide_and_Conquer import *

print("\n")
hf.print_console_menu() 
algorithm_choice = input("\nEnter number corresponding to algorithm you want to see: ") 
algorithm_choice = int(algorithm_choice)
print("NOTE: Graphics based option will open new window either in background or foreground")
print("\tI can guarantee foreground on mac, don't know about windows\n")
if algorithm_choice == 4:
    print("Binary Tree Sort:")
    binary_tree_sort()
    exit()

test_arr = list(range(1, 7))
random.shuffle(test_arr)

pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
window = pygame.display.set_mode((c.WIN_WIDTH, c.WIN_HEIGHT)) # (width, height)
# window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("That's not a bug, its a feature")

running = True
clock = pygame.time.Clock()

while running:    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if algorithm_choice == 1:
        running = bubble_sort.graphic_bubble_sort(window,test_arr)
    elif algorithm_choice == 2:
        running = graphic_selection_sort(window, test_arr)
    elif algorithm_choice == 3:
        running = graphic_closest_pair(window, num_points=10)

    if running == False:
        time.sleep(3)
    if algorithm_choice != 4:
        pygame.display.flip() #* Updates window contents, keep at bottom

print("\nThanks for using the visualizer!")