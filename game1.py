import pygame, sys, random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)

# Game variables
gravity = 0.5
bird_movement = 0
score = 0
game_active = True

# Load images
bird_surface = pygame.Surface((34, 24))
bird_surface.fill((255, 255, 0))
bird_rect = bird_surface.get_rect(center=(100, HEIGHT // 2))

pipe_surface = pygame.Surface((52, 400))
pipe_surface.fill(GREEN)
pipe_list = []

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

pipe_height = [300, 350, 400, 450]

# Functions
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= HEIGHT:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
    return [pipe for pipe in pipes if pipe.right > -50]

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= HEIGHT:
        return False
    return True

def display_score(score):
    score_surface = font.render(f"Score: {int(score)}", True, WHITE)
    score_rect = score_surface.get_rect(center=(WIDTH//2, 50))
    screen.blit(score_surface, score_rect)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active:
                    bird_movement = 0
                    bird_movement -= 8
                else:
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (100, HEIGHT // 2)
                    bird_movement = 0
                    score = 0
        if event.type == SPAWNPIPE:
            random_pipe_pos = random.choice(pipe_height)
            bottom_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos))
            top_pipe = pipe_surface.get_rect(midbottom=(500, random_pipe_pos - 150))
            pipe_list.extend([bottom_pipe, top_pipe])

    # Background
    screen.fill(BLUE)

    if game_active:
        # Bird movement
        bird_movement += gravity
        bird_rect.centery += int(bird_movement)
        screen.blit(bird_surface, bird_rect)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Collision
        game_active = check_collision(pipe_list)

        # Score
        score += 0.01
        display_score(score)

    else:
        game_over_surface = font.render("Game Over!", True, WHITE)
        game_over_rect = game_over_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(game_over_surface, game_over_rect)
        display_score(score)

    # Update screen
    pygame.display.update()
    clock.tick(60)
