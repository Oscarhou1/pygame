# -----------------------------------------------------------------------------
# COLOUR LAB - PLAID
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# The plaid must have 2 different colours
# LEVEL 4
# Everything listed in level 3 
# The plaid has 2 different strokeWeights
# LEVEL 4+
# Everything listed in level 4
# The plaid uses alpha colour
# 
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# 
# Challenge Difficulty:**
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to github when finished
# 
# Good luck!
#-----------------------------------------------------------------------------
import pygame
import random

# Initialize Pygame
pygame.init()

# *********SETUP**********
windowWidth = 500
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  # will allow us to set framerate

# Colors (Two different colors for plaid)
color1 = (255, 0, 0)  # Red
color2 = (0, 255, 0)  # Green

# Line thicknesses
line_thickness_1 = 10  # Thicker lines for vertical lines
line_thickness_2 = 5   # Thinner lines for horizontal lines

# *********GAME LOOP**********
while True:
    # *********EVENTS**********
    for ev in pygame.event.get():  # Look for any event
        if ev.type == pygame.QUIT:  # window close button clicked?
            pygame.quit()  # Quit the game
            exit()

    # *********GAME LOGIC**********
    # *********DRAW THE FRAME**********
    window.fill((0, 0, 0))  # Fill the screen with black to clear previous frame

    # Drawing the plaid pattern using for loops
    # Horizontal lines (alternating colors and thicknesses)
    for y in range(0, windowHeight, line_thickness_2 * 2):
        color = color1 if (y // (line_thickness_2 * 2)) % 2 == 0 else color2
        pygame.draw.rect(window, color, pygame.Rect(0, y, windowWidth, line_thickness_2))

    # Vertical lines (alternating colors and thicknesses)
    for x in range(0, windowWidth, line_thickness_1 * 2):
        color = color2 if (x // (line_thickness_1 * 2)) % 2 == 0 else color1
        pygame.draw.rect(window, color, pygame.Rect(x, 0, line_thickness_1, windowHeight))

    # *********SHOW THE FRAME TO THE USER**********
    pygame.display.flip()
    clock.tick(60)  # Force frame rate to 60fps or lower


