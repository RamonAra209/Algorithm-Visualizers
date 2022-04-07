import math
import time

import pygame
import constants as c
from help_functions import add_recs_to_screen, create_font_object, create_rects_on_list

test_arr = [3, 2, 4, 1, 5, 6, 8, 7] # len = 6

def merge_sort(a:list):
    n = len(a)
    b = []
    c = []
    bound = math.floor(n / 2)
    if n > 1:
        b[0:bound] = a[0:bound]
        c[0:bound] = a[bound:n]
        merge_sort(b)
        merge_sort(c)
        merge(b, c, a) 
    return a
    
def merge(b:list, c:list, a:list):
    i, j, k = 0, 0, 0
    p = len(b)
    q = len(c)

    while i < p and j < q:
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        
        k += 1

    if i == p:
        a[k:(p+q)] = c[j:q]
    else:
        a[k:(p+q)] = b[i:p]
    
    return a

def graphic_merge_sort(window, arr): #* NOTE: Not going to use recursion for graphic implementation
    n = len(arr)
    header, header_rect = create_font_object("Merge Sort", c.BLACK)
    header_rect.center = (c.HEADER_X, c.HEADER_Y)

    # initial array adding to screen
    x_pos = c.WIN_WIDTH / 2 - (len(arr) * 50)
    y_pos = c.WIN_HEIGHT / 2 - 100
    nums_dict = create_rects_on_list(arr, x_pos, y_pos)
    condensed_draw(window, header, header_rect)
    add_recs_to_screen(window, nums_dict)
    # draw_split(window, arr, nums_dict)
    pygame.display.flip()
    recursive_split(window, arr, nums_dict, counter=math.floor(math.log2(n)))
    pygame.display.flip()
    time.sleep(1)
    return False

def recursive_split(window, arr:list, nums_dict:dict[int, pygame.Rect], counter):
    n = len(arr)
    if n == 1:
        return
    split_point = math.ceil(n / 2)
    left = arr[:split_point]
    print(f"{arr} --> {left}")
    right = arr[split_point:]
    
    move_origin_rect(left, nums_dict, counter, isLeftArr=True)
    move_origin_rect(right, nums_dict, counter, isLeftArr=False)
    left_rect = nums_dict[left[0]]
    right_rect = nums_dict[right[0]]
    add_recs_to_screen(window, create_rects_on_list(left, left_rect.left, left_rect.top))
    add_recs_to_screen(window, create_rects_on_list(right, right_rect.left, right_rect.top))
    pygame.display.flip()
    time.sleep(0.5) # timer to show recursive steps
    
    recursive_split(window, arr=left, nums_dict=nums_dict, counter=counter-1)
    recursive_split(window, arr=right, nums_dict=nums_dict, counter=counter-1)

def move_origin_rect(arr:int, nums_dict:dict[int, pygame.Rect], counter:int, isLeftArr=True):
    x_offset_left = -50 * counter
    x_offset_right = 50 * counter
    if len(arr) == 1:
        x_offset_left, x_offset_right = -10, 10
    for i in range(len(arr)):
        if isLeftArr:
            nums_dict[arr[i]].move_ip(x_offset_left, 125)
        else:
            nums_dict[arr[i]].move_ip(x_offset_right, 125)
        
def condensed_draw(window, header, header_rect):
    window.fill(c.BACKGROUND_COLOR)
    window.blit(header, header_rect)

def draw_split(window, arr:list, nums_dict: dict):
    n = len(nums_dict)
    if n == 1:
        return
    split_point = math.ceil(n / 2) 
    rect = pygame.Rect
    if n != 1:
        rect =  nums_dict[arr[split_point]]
    if n / 2 == 0:
        pygame.draw.line(window, c.RED, rect.topright, rect.bottomright, width=4)
    else:
        pygame.draw.line(window, c.RED, rect.topleft, rect.bottomleft, width=4)
