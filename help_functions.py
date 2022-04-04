import pygame
from pygame import Rect
import constants as c

def create_rects_on_list(arr:list[int], win_width, win_height):
    num_dict = {} # Dict = {key=int_in_arr, val=Rect_Object}
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
        pygame.draw.rect(window, c.BLACK, rect, width=5) # draws square on screen

        rect = pygame.Rect.move(rect, 40, 35)
        window.blit(temp_text, rect) # adds number to screen
        
def update_rects_positions(rects:dict):
    for rect in rects.values():
        rect = pygame.Rect.move(rect, 40, 35)
    return rects
    
###* Visualizer Labels
def swap_indices(window, rects:dict, ind_one, ind_two):
    #keep in mind the dict is key=num, val=Rect
    rects[ind_one], rects[ind_two] = rects[ind_two], rects[ind_one]
    draw_swap_labels(window, rects[ind_one], rects[ind_two], ind_one, ind_two)
    return rects

def draw_swap_labels(window, rect_one:pygame.Rect, rect_two:pygame.Rect, val_one, val_two):
    xy_rect_one = ((rect_one.left + rect_one.right)/2, rect_one.bottom + 30)
    xy_rect_two = ((rect_two.left + rect_two.right)/2, rect_two.bottom + 30)
    pygame.draw.line(window, c.RED, xy_rect_one, xy_rect_two, width=3)

    pygame.draw.line(window, c.RED, ((rect_one.left + rect_one.right)/2, rect_one.bottom + 30),
                                  ((rect_one.left + rect_one.right)/2, rect_one.bottom + 10), width=3) 
    
    pygame.draw.line(window, c.RED, ((rect_two.left + rect_two.right)/2, rect_two.bottom + 30),
                                  ((rect_two.left + rect_two.right)/2, rect_two.bottom + 10), width=3) 

    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render(f"Swapping {val_one} and {val_two}", True, c.RED)
    text_rect = text.get_rect()
    text_rect.center = (c.WIN_WIDTH / 2, c.WIN_HEIGHT/2 + 130)
    window.blit(text, text_rect)
    pygame.display.flip()
    
         
def draw_iterator_label(window, iter_label:str, rect:pygame.Rect, above=True):  
    y_val = None
    if iter_label == "i":
        y_val = rect.top - 30
    elif iter_label == "j":
        y_val = rect.top - 80
    iter_position = ((rect.left + rect.right)/2, y_val)
    text, text_rect = create_font_object(iter_label, c.RED)
    text_rect.center = iter_position
    window.blit(text, text_rect)
    pygame.display.flip()
    
def draw_header(window, header_text, header_rect):
    window.blit(header_text, header_rect)
    pygame.display.flip()
    
def create_font_object(string:str, color):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f"{string}", True, color)
    text_rect = text.get_rect()
    return text, text_rect



###* Graph Based Problems
