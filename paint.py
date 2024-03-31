import pygame
import sys

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
draw_circle = False
rect_start = None
circle_center = None

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
                draw_circle = True
                circle_center = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
            elif event.button == 3:
                draw_rectangle = False
            elif event.button == 2:
                draw_circle = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing and not draw_rectangle and not draw_circle:
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
            elif draw_circle: 
                if circle_center:
                    if pygame.key.get_pressed()[pygame.K_e]:  
                        pygame.draw.circle(screen, WHITE, circle_center, max(abs(event.pos[0] - circle_center[0]), abs(event.pos[1] - circle_center[1])), brush_size)
                    else:
                        pygame.draw.circle(screen, brush_color, circle_center, max(abs(event.pos[0] - circle_center[0]), abs(event.pos[1] - circle_center[1])), brush_size)

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