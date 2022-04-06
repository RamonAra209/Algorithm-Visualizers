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
    
    return index1, index2

def graphic_closest_pair(window, num_points):
    header, header_rect = hf.create_font_object("Closest Pair (Brute Force)", c.BLACK) 
    header_rect.center = (c.WIN_WIDTH/2, 75)
    left, top = 100, 100
    width, height = c.WIN_WIDTH - 200, c.WIN_HEIGHT - 300
    border_rect = pygame.Rect(left, top, width, height)

    points = generate_points(num_points, left, top, width, height)
    condensed_draw(window, points, header, header_rect, border_rect)
    
    n = len(points)
    dmin = math.inf 
    d = None
    index1, index2 = None, None
    for i in range(0, n-1):
        for j in range(i+1, n):
            condensed_draw(window, points, header, header_rect, border_rect)
            x_i, y_i = points[i].x, points[i].y
            x_j, y_j = points[j].x, points[j].y
            d = math.sqrt((x_i - x_j)**2 + (y_i - y_j)**2) 
            if index1 != None:
                pygame.draw.line(window, c.BLUE, points[index1].get_point(), points[index2].get_point(), width=3)
            pygame.draw.line(window, c.RED, points[i].get_point(), points[j].get_point(), width=3) 
            pygame.display.flip()
            time.sleep(0.025)
            if d < dmin:
                condensed_draw(window, points, header, header_rect, border_rect)
                pygame.draw.line(window, c.BLUE, points[i].get_point(), points[j].get_point(), width=3)
                pygame.display.flip()
                dmin = d
                index1 = i
                index2 = j
                time.sleep(0.50)

    condensed_draw(window, points, header, header_rect, border_rect)
    pygame.draw.line(window, c.GREEN, points[index1].get_point(), points[index2].get_point(), width=3)
    correct_text, correct_rect = hf.create_font_object("Found Shortest Path", c.GREEN)
    correct_rect.center = (c.WIN_WIDTH/2, c.WIN_HEIGHT - 150)
    window.blit(correct_text, correct_rect)
    pygame.display.flip()
    time.sleep(3)
    return False

def condensed_draw(window, points:list, header, header_rect, border_rect):
    window.fill(c.BACKGROUND_COLOR)
    window.blit(header, header_rect)
    pygame.draw.rect(window, c.BLACK, border_rect, width=5) 
    hf.draw_points(window, points)

def generate_points(num_points:int, left, top, width, height) -> list[hf.Point]:
    points = []
    for i in range(num_points):
        x = random.randint(left + 10, width + 90) 
        y = random.randint(top + 10, height + 90)
        points.append(hf.Point(x, y))
    return points