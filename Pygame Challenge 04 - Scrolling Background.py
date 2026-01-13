# -----------------------------------------------------------------------------
# ANIMATION LAB - SCROLLING BACKGROUND
#
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
#
# Lab Requirements:
# LEVEL 3
# A background that scrolls across the screen creating the illusion of movement
# LEVEL 4+
# Everything listed in level 3
# Multiple layers moving at different speeds to create the parallax effect, like you see to the left
#
# Recommended Lessons:
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# Pygame Images
# Pygame Animation
#
# Challenge Difficulty:*
#
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
#
# Upload your code to githunb when finished
#
# Good luck!
#-----------------------------------------------------------------------------
import pygame
pygame.init()

# ---------- SETTINGS ----------
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parallax Scrolling - Level 4")
clock = pygame.time.Clock()
FPS = 60

# ---------- LOAD IMAGES ----------
sky = pygame.image.load("sky.jpg")
mountains = pygame.image.load("mountains.jpg")
ground = pygame.image.load("ground.jpg")

sky = pygame.transform.scale(sky, (400, 300))
mountains = pygame.transform.scale(mountains, (800,400))
ground = pygame.transform.scale(ground, (WIDTH, HEIGHT))

# ---------- START POSITIONS ----------
sky_x = 0
mountain_x = 0
ground_x = 0

# ---------- SPEEDS (parallax) ----------
sky_speed = 1        # far = slow
mountain_speed = 2
ground_speed = 4     # close = fast

# ---------- GAME LOOP ----------
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move backgrounds
    sky_x -= sky_speed
    mountain_x -= mountain_speed
    ground_x -= ground_speed

    # reset when off screen
    if sky_x <= -WIDTH:
        sky_x = 0
    if mountain_x <= -WIDTH:
        mountain_x = 0
    if ground_x <= -WIDTH:
        ground_x = 0

    # draw background twice (for looping)
    screen.blit(sky, (sky_x, 0))
    screen.blit(sky, (sky_x + WIDTH, 0))

    screen.blit(mountains, (mountain_x, 0))
    screen.blit(mountains, (mountain_x + WIDTH, 0))

    screen.blit(ground, (ground_x, 0))
    screen.blit(ground, (ground_x + WIDTH, 0))

    pygame.display.update()

pygame.quit()
