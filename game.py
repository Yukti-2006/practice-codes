import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)

# Game variables
gravity = 0.5
bird_movement = 0
game_active = True
score = 0

# Load bird image (simple rectangle instead)
bird = pygame.Rect(100, 300, 30, 30)

# Pipe settings
pipe_width = 70
pipe_gap = 150
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# Clock
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(win, GREEN, pipe)

def create_pipe():
    height = random.randint(150, 450)
    top_pipe = pygame.Rect(WIDTH, height - pipe_gap - 400, pipe_width, 400)
    bottom_pipe = pygame.Rect(WIDTH, height, pipe_width, 400)
    return top_pipe, bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
    return [pipe for pipe in pipes if pipe.right > 0]

def check_collision(pipes):
    for pipe in pipes:
        if bird.colliderect(pipe):
            return False
    if bird.top <= 0 or bird.bottom >= HEIGHT:
        return False
    return True

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = -8
            if event.key == pygame.K_SPACE and not game_active:
                # Restart game
                game_active = True
                pipe_list.clear()
                bird.center = (100, 300)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    win.fill(BLUE)

    if game_active:
        # Bird
        bird_movement += gravity
        bird.centery += int(bird_movement)
        pygame.draw.ellipse(win, (255, 255, 0), bird)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Collision check
        game_active = check_collision(pipe_list)

        # Score
        for pipe in pipe_list:
            if pipe.centerx == bird.centerx:
                score += 0.5  # each pair of pipes gives +1 total

        score_text = font.render(f"Score: {int(score)}", True, WHITE)
        win.blit(score_text, (10, 10))

    else:
        # Game over screen
        msg = font.render("Game Over! Press SPACE to Restart", True, WHITE)
        win.blit(msg, (20, HEIGHT // 2 - 20))

    pygame.display.update()
    clock.tick(60)