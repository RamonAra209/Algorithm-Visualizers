import pygame
import constants as c
import help_functions as hf 
import time
import random

def selection_sort(arr:list) -> list:
    n = len(arr)
    for i in range(0, n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

def graphic_selection_sort(window, arr:list):
    header, header_rect = hf.create_font_object("Selection Sort", c.BLACK)
    header_rect.center = (c.WIN_WIDTH/2, 75)
    
    n = len(arr)
    x_pos = c.WIN_WIDTH / 2 - (len(arr) * 50)
    y_pos = c.WIN_HEIGHT / 2 - 100
    num_dict = hf.create_rects_on_list(arr, x_pos, y_pos)
    
    for i in range(0, n):
        min = i
        window.fill(c.BACKGROUND_COLOR)
        hf.draw_header(window, header, header_rect)
        hf.add_recs_to_screen(window, num_dict)
        hf.draw_iterator_label(window, "i", num_dict[arr[i]])
        
        for j in range(i+1, n):
            timer_flag = False
            window.fill(c.BACKGROUND_COLOR)
            hf.draw_header(window, header, header_rect)
            hf.add_recs_to_screen(window, num_dict)
            hf.draw_iterator_label(window, "i", num_dict[arr[i]])
            hf.draw_iterator_label(window, "j", num_dict[arr[j]])
            if arr[j] < arr[min]:
                min = j
            if timer_flag == False:
                time.sleep(c.SLEEP_TIME)
                window.fill(c.BACKGROUND_COLOR)
                hf.draw_header(window, header, header_rect)
                hf.add_recs_to_screen(window, num_dict)
                hf.draw_iterator_label(window, "i", num_dict[arr[i]])
                hf.draw_iterator_label(window, "j", num_dict[arr[j]])
        arr[i], arr[min], = arr[min], arr[i]
        window.fill(c.BACKGROUND_COLOR)
        hf.draw_header(window, header, header_rect)
        hf.add_recs_to_screen(window, num_dict)
        hf.draw_iterator_label(window, "i", num_dict[arr[i]])    
        hf.draw_iterator_label(window, "j", num_dict[arr[j]])
        num_dict= hf.swap_indices(window, num_dict, arr[i], arr[min])
        time.sleep(c.SLEEP_TIME)
    
    text, text_rect = hf.create_font_object("Successfully Sorted", [0, 255, 0])
    text_rect.center = (c.WIN_WIDTH/2, c.WIN_HEIGHT/2 + 130)
    window.fill(c.BACKGROUND_COLOR)
    hf.draw_header(window, header, header_rect)
    hf.add_recs_to_screen(window, num_dict)
    window.blit(text, text_rect)
    pygame.display.flip()

    return False
