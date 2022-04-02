import help_functions as hf
from .. import constants as c
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
    hf.add_recs_to_screen(window, num_dict)
             