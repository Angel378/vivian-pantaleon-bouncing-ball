import pygame
import random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball - VIVIAN")
clock = pygame.time.Clock()

# Font setup
font = pygame.font.SysFont("Arial", 22, bold=True)

# Ball properties
ball_radius = 45  # Medium size
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
ball_dx = 5
ball_dy = 4

# Ball color options
ball_colors = [
    (0, 0, 255),       # Blue
    (255, 0, 0),       # Red
    (0, 100, 0),       # Dark Green
    (138, 43, 226),    # Violet
    (255, 255, 0)      # Yellow
]
ball_color = random.choice(ball_colors)

# Background color
bg_color = (255, 255, 255)  # White

# Main game loop
running = True
while running:
    clock.tick(60)
    screen.fill(bg_color)

    # Handle quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    bounced = False

    # Bounce on X walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_dx *= -1
        bounced = True

    # Bounce on Y walls
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_dy *= -1
        bounced = True

    # Change ball color on bounce
    if bounced:
        ball_color = random.choice(ball_colors)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Draw "VIVIAN" text inside (double color: white shadow + black)
    text_shadow = font.render("VIVIAN", True, (255, 255, 255))  # White shadow
    text_main = font.render("VIVIAN", True, (0, 0, 0))          # Black text
    text_rect = text_main.get_rect(center=(ball_x, ball_y))
    screen.blit(text_shadow, (text_rect.x + 2, text_rect.y + 2))  # Slight offset for shadow
    screen.blit(text_main, text_rect)

    # Update display
    pygame.display.flip()

pygame.quit()
