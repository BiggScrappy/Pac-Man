import pygame
import math
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pac-Man')

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Game settings
pacman_radius = 30
pacman_x, pacman_y = width // 2, height // 2
mouth_angle = 45  # Angle for mouth
pacman_speed = 5

# Pellets
pellet_radius = 5
pellets = [(random.randint(50, width-50), random.randint(50, height-50)) for _ in range(10)]

# Create a font
font = pygame.font.SysFont('Arial', 24)

# Function to draw the Pac-Man character with a correct mouth
def draw_pacman(screen, x, y, radius, mouth_angle):
    # Draw the yellow circle for Pac-Man's body
    pygame.draw.circle(screen, YELLOW, (x, y), radius)
    
    # Create the "mouth" as a black triangle (using a polygon)
    # Pac-Man's mouth is like a wedge, starting from a certain angle
    mouth_width = int(radius * 1.5)
    mouth_height = int(radius * 1.5)
    mouth_points = [
        (x, y),
        (x + mouth_width * math.cos(math.radians(mouth_angle)), y - mouth_height * math.sin(math.radians(mouth_angle))),
        (x + mouth_width * math.cos(math.radians(-mouth_angle)), y - mouth_height * math.sin(math.radians(-mouth_angle)))
    ]
    
    # Draw the black mouth
    pygame.draw.polygon(screen, BLACK, mouth_points)

# Main game loop
running = True
score = 0

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed
    
    # Check if Pac-Man eats any pellets
    for pellet in pellets[:]:
        if math.sqrt((pacman_x - pellet[0])**2 + (pacman_y - pellet[1])**2) < pacman_radius + pellet_radius:
            pellets.remove(pellet)
            score += 10
    
    # Draw Pac-Man and the pellets
    draw_pacman(screen, pacman_x, pacman_y, pacman_radius, mouth_angle)
    for pellet in pellets:
        pygame.draw.circle(screen, WHITE, pellet, pellet_radius)
    
    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)

# Quit pygame
pygame.quit()
