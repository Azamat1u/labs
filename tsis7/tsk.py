import pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Drawer")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define shapes
rect = pygame.Rect(50, 50, 100, 100)
circle = pygame.Rect(250, 50, 100, 100)
line_start = (450, 50)
line_end = (550, 150)

# Set initial colors
rect_color = BLACK
circle_color = BLACK
line_color = BLACK

running = True
while running:
    screen.fill(WHITE)
    
    # Draw shapes
    pygame.draw.rect(screen, rect_color, rect)
    pygame.draw.ellipse(screen, circle_color, circle)
    pygame.draw.line(screen, line_color, line_start, line_end, 5)
    
    # changing colors of shapes by buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Change rect color to red
                rect_color = RED
            elif event.key == pygame.K_g:  # Change circle color to green
                circle_color = GREEN
            elif event.key == pygame.K_b:  # Change line color to blue
                line_color = BLUE
            elif event.key == pygame.K_w:  # Change all shapes color to white
                rect_color = WHITE
                circle_color = WHITE
                line_color = WHITE
    
    pygame.display.flip()