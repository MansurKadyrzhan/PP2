import random
import pygame as pg

WSIZE = (720, 480)
screen = pg.display.set_mode(WSIZE)

TSIDE = 30
MSIZE = WSIZE[0] // TSIDE, WSIZE[1] // TSIDE

start_pos = MSIZE[0] // 2, MSIZE[1] // 2
snake = [start_pos]
alive = True

direction = 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

fps = 5
clock = pg.time.Clock()

pg.font.init()
font_score = pg.font.SysFont("Arial", 25)
font_gameover = pg.font.SysFont("Arial", 45)
font_space = pg.font.SysFont("Arial", 18)

# Define food types with weights
food_types = [("red", 0.6), ("blue", 0.3), ("yellow", 0.1)]
current_food = None
food_timer = 0
food_duration = 5000  # Duration in milliseconds

running = True
while running:
    clock.tick(fps)
    screen.fill("black")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if alive:
                if event.key == pg.K_RIGHT and direction != 2:
                    direction = 0
                if event.key == pg.K_DOWN and direction != 3:
                    direction = 1
                if event.key == pg.K_LEFT and direction != 0:
                    direction = 2
                if event.key == pg.K_UP and direction != 1:
                    direction = 3
            else:
                if event.key == pg.K_SPACE:
                    alive = True
                    snake = [start_pos]
                    fps = 5
                    # Reset food timer and generate new food
                    food_timer = 0
                    current_food = None

    # Draw snake
    [pg.draw.rect(screen, "green", (x * TSIDE, y * TSIDE, TSIDE - 1, TSIDE - 1)) for x, y in snake]

    # Handle food generation and disappearance
    if alive:
        if current_food is None:
            # Generate new food after a certain time
            if food_timer <= 0:
                food_type = random.choices(population=[food[0] for food in food_types], weights=[food[1] for food in food_types])[0]
                current_food = (random.randint(0, MSIZE[0]-1), random.randint(0, MSIZE[1]-1)), food_type
                food_timer = food_duration
            else:
                food_timer -= clock.get_time()
        else:
            # Draw and check if food should disappear
            pg.draw.rect(screen, current_food[1], (current_food[0][0] * TSIDE, current_food[0][1] * TSIDE, TSIDE - 1, TSIDE - 1))
            food_timer -= clock.get_time()
            if food_timer <= 0:
                current_food = None
                food_timer = 0

    # Handle snake movement and collision
    if alive:
        new_pos = snake[0][0] + directions[direction][0], snake[0][1] + directions[direction][1]
        if not (0 <= new_pos[0] < MSIZE[0] and 0 <= new_pos[1] < MSIZE[1]) or new_pos in snake:
            alive = False
        else:
            snake.insert(0, new_pos)
            # Check if snake eats food
            if current_food and new_pos == current_food[0]:
                fps += 1
                current_food = None
            else:
                snake.pop(-1)
    else:
        text = font_gameover.render(f"GAME OVER", True, "white")
        screen.blit(text, (WSIZE[0] // 2 - text.get_width() // 2, WSIZE[1] // 2 - 50))
        text = font_space.render(f"Press SPACE for restart", True, "white")
        screen.blit(text, (WSIZE[0] // 2 - text.get_width() // 2, WSIZE[1] // 2 + 10))
    screen.blit(font_score.render(f"Score: {len(snake)}", True, "yellow"), (5, 5))

    pg.display.flip()