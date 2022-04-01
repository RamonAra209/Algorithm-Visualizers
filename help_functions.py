
import pygame
from pygame import Rect

BLACK = [0, 0, 0]
test_arr = [1, 2, 3]

def create_rects_on_list(arr:list[int], win_width, win_height):
    num_dict = {}
    len_arr = len(arr)
    
    r_width, r_height = 100, 100
    starting_x = win_width / 2 - (len(arr) * 50)
    starting_y = win_height / 2 - 100    
    for i in range(0, len_arr):
        left = starting_x + (i * r_width)
        top = starting_y
        temp_rect = pygame.Rect((left, top), (r_width, r_height))
        num_dict[arr[i]] = temp_rect
    return num_dict


def add_recs_to_screen(window, rects:dict):
    font = pygame.font.Font('freesansbold.ttf', 32)
    for num, rect in rects.items():
        temp_text = font.render(str(num), True, [0, 0, 0])
        pygame.draw.rect(window, BLACK, rect, width=5) # draws square on screen
        
        rect = pygame.Rect.move(rect, 40, 35)
        window.blit(temp_text, rect) # adds number to screen
        
        
#? Idea on how to move blocks
#? Since we saved the Rect object (i.e, positional values)
#? We can just swap the the Rect Object values when you perform swaps in [x] Sorting Algorithm