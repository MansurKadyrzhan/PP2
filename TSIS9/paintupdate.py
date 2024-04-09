import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

brush_size = 10
brush_color = BLACK

drawing = False
draw_rectangle = False
draw_square = False
draw_triangle = False
draw_rhombus = False

rect_start = None
square_start = None
triangle_start = None
rhombus_start = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                drawing = True
            elif event.button == 3:  
                draw_rectangle = True
                rect_start = event.pos
            elif event.button == 2:
                draw_square = True
                square_start = event.pos
            elif event.button == 4:
                draw_triangle = True
                triangle_start = event.pos
            elif event.button == 5:
                draw_rhombus = True
                rhombus_start = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
            elif event.button == 3:
                draw_rectangle = False
            elif event.button == 2:
                draw_square = False
            elif event.button == 4:
                draw_triangle = False
            elif event.button == 5:
                draw_rhombus = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing and not draw_rectangle and not draw_square and not draw_triangle and not draw_rhombus:
                if pygame.key.get_pressed()[pygame.K_e]:  
                    pygame.draw.circle(screen, WHITE, event.pos, brush_size)
                else:
                    pygame.draw.circle(screen, brush_color, event.pos, brush_size)
            elif draw_rectangle:  
                if rect_start:
                    rect_end = event.pos
                    if pygame.key.get_pressed()[pygame.K_e]:
                        pygame.draw.rect(screen, WHITE, (rect_start, (rect_end[0]-rect_start[0], rect_end[1]-rect_start[1])), brush_size)
                    else:
                        pygame.draw.rect(screen, brush_color, (rect_start, (rect_end[0]-rect_start[0], rect_end[1]-rect_start[1])), brush_size)
            elif draw_square:
                if square_start:
                    square_end = event.pos
                    side_length = max(abs(square_end[0] - square_start[0]), abs(square_end[1] - square_start[1]))
                    if pygame.key.get_pressed()[pygame.K_e]:
                        pygame.draw.rect(screen, WHITE, (square_start, (side_length, side_length)), brush_size)
                    else:
                        pygame.draw.rect(screen, brush_color, (square_start, (side_length, side_length)), brush_size)
            elif draw_triangle:
                if triangle_start:
                    triangle_end = event.pos
                    if pygame.key.get_pressed()[pygame.K_e]:
                        pygame.draw.polygon(screen, WHITE, [(triangle_start[0], triangle_end[1]), triangle_end, (triangle_end[0], triangle_start[1])], brush_size)
                    else:
                        pygame.draw.polygon(screen, brush_color, [(triangle_start[0], triangle_end[1]), triangle_end, (triangle_end[0], triangle_start[1])], brush_size)
            elif draw_rhombus:
                if rhombus_start:
                    rhombus_end = event.pos
                    diagonal_length = math.sqrt((rhombus_end[0] - rhombus_start[0]) ** 2 + (rhombus_end[1] - rhombus_start[1]) ** 2)
                    if pygame.key.get_pressed()[pygame.K_e]:
                        pygame.draw.polygon(screen, WHITE, [(rhombus_start[0], rhombus_start[1] + diagonal_length/2), (rhombus_start[0] + diagonal_length/2, rhombus_start[1]), (rhombus_end[0], rhombus_start[1] - diagonal_length/2), (rhombus_start[0] - diagonal_length/2, rhombus_start[1])], brush_size)
                    else:
                        pygame.draw.polygon(screen, brush_color, [(rhombus_start[0], rhombus_start[1] + diagonal_length/2), (rhombus_start[0] + diagonal_length/2, rhombus_start[1]), (rhombus_end[0], rhombus_start[1] - diagonal_length/2), (rhombus_start[0] - diagonal_length/2, rhombus_start[1])], brush_size)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                brush_size += 1
            elif event.key == pygame.K_DOWN:
                brush_size = max(1, brush_size - 1)
            elif event.key == pygame.K_c:
                screen.fill(WHITE)
            elif event.key == pygame.K_r:
                brush_color = RED
            elif event.key == pygame.K_g:
                brush_color = GREEN
            elif event.key == pygame.K_b:
                brush_color = BLUE

    pygame.display.flip()