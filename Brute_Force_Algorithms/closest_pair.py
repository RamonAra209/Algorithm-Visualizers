import pygame, math, time, random
import constants as c
import help_functions as hf

        
def closest_points(points:list):
    n = len(points)

    dmin = math.inf 
    d = None
    index1, index2 = None, None
    for i in range(0, n-1):
        for j in range(i+1, n):
           x_i, y_i = points[i].x, points[i].y
           x_j, y_j = points[j].x, points[j].y
           d = math.sqrt((x_i - x_j)**2 + (y_i - y_j)**2) 
           if d < dmin:
               dmin = d
               index1 = i
               index2 = j
    
    print(f"Shortest Path Calculated was {d} between pairs:")
    print(f"\tpair1: {points[index1].x}, {points[index1].y}")
    print(f"\tpair2: {points[index2].x}, {points[index2].y}")
    return index1, index2

def graphic_closest_pair(window, points:list):
    header, header_rect = hf.create_font_object("Closest Pair (Brute Force)", c.BLACK) 
    header_rect.center = (c.WIN_WIDTH/2, 75)
    left, top = 100, 100
    width, height = c.WIN_WIDTH - 200, c.WIN_HEIGHT - 300
    border_rect = pygame.Rect(left, top, width, height) 

    points = []
    for i in range(10):
        x = random.randint(left + 10, width - 10) 
        y = random.randint(top + 10, height - 10)
        points.append(hf.Point(x, y))
    
    condensed_draw(window, points, header, header_rect, border_rect)
    
    n = len(points)
    dmin = math.inf 
    d = None
    index1, index2 = None, None
    index1, index2 = 1, 2
    for i in range(0, n-1):
        for j in range(i+1, n):
            condensed_draw(window, points, header, header_rect, border_rect)
            x_i, y_i = points[i].x, points[i].y
            x_j, y_j = points[j].x, points[j].y
            d = math.sqrt((x_i - x_j)**2 + (y_i - y_j)**2) 
            pygame.draw.line(window, c.RED, points[i].get_point(), points[j].get_point(), width=3) 
            pygame.display.flip()
            time.sleep(0.1)
            if d < dmin:
                condensed_draw(window, points, header, header_rect, border_rect)
                pygame.draw.line(window, c.BLUE, points[i].get_point(), points[j].get_point(), width=3)
                pygame.display.flip()
                dmin = d
                index1 = i
                index2 = j
                time.sleep(0.55)

    condensed_draw(window, points, header, header_rect, border_rect)
    pygame.draw.line(window, c.GREEN, points[index1].get_point(), points[index2].get_point(), width=3)
    pygame.display.flip()
    time.sleep(3)
    return False

def condensed_draw(window, points:list, header, header_rect, border_rect):
    window.fill(c.BACKGROUND_COLOR)
    window.blit(header, header_rect)
    pygame.draw.rect(window, c.BLACK, border_rect, width=5) 
    hf.draw_points(window, points)