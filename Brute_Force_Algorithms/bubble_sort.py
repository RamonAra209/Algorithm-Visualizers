import help_functions as hf
import constants as c
import time
import pygame
#* Original Bubble Sort
#? Best Case: n^2
#? Worst Case: n^2
def bubble_sort(arr:list) -> list:
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#* Graphical Implementation of Bubble Sort
def graphic_bubble_sort(window, arr:list):
    n = len(arr)
    num_dict = hf.create_rects_on_list(arr, c.WIN_WIDTH, c.WIN_HEIGHT)
    for i in range(0, n):
        window.fill(c.BACKGROUND_COLOR)
        hf.add_recs_to_screen(window, num_dict)
        hf.draw_iterator_label(window, "i", num_dict[arr[i]])
        for j in range(0, n-i-1):
            window.fill(c.BACKGROUND_COLOR)
            hf.draw_iterator_label(window, "i", num_dict[arr[i]])
            hf.draw_iterator_label(window, "j", num_dict[arr[j]])
            hf.add_recs_to_screen(window, num_dict)
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                window.fill(c.BACKGROUND_COLOR)
                hf.draw_iterator_label(window, "i", num_dict[arr[i]])    
                hf.draw_iterator_label(window, "j", num_dict[arr[j]])
                hf.add_recs_to_screen(window, num_dict)
                num_dict= hf.swap_indices(window, num_dict, arr[j], arr[j+1])
                time.sleep(0.75)
        
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Successfully sorted", True, [0, 255, 0])
        text_rect = text.get_rect()
        text_rect.center = (c.WIN_WIDTH/2, c.WIN_HEIGHT/2 + 130)
        window.fill(c.BACKGROUND_COLOR)
        hf.add_recs_to_screen(window, num_dict)
        window.blit(text, text_rect)
        pygame.display.flip()
        
    return False
test_arr = [9, 1, 7, 2, 99]
print(bubble_sort(test_arr))