# -----------------------------------------------------------------------------
# GAMESTATE LAB - MENU
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# A minimum of 3 possible unique backdrops
# A minimum of 2 buttons that when clicked will change the view of the user
# A method to return to the main menu
# HTML Buttons
# Uses gamestates
# LEVEL 4
# A minimum of 4 possible unique windows
# A minimum of 3 buttons that when clicked will change the backdrop or view of the user
# A method to return to the main menu
# Use gamestates
# Collision detection style buttons
# LEVEL 4+
# Everything listed in level 3 and 4
# Add sound effects when the button is pressed or add a mouseover effect to the button (the button highlights or changes looks when the mouse goes over the locations of the button)
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
# Pygame Sounds
# Pygame The Game Loop
# Pygame Events
# Pygame Gamestates
# Pygame Collision Detection
# Pygame Sprites
# 
# Challenge Difficulty:****
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to github when finished
# 
# Good luck!
#-----------------------------------------------------------------------------
import pygame
pygame.init()

# ---------- SETUP ----------
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gamestate Menu Lab")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# ---------- GAME STATES ----------
MENU = "menu"
SCREEN1 = "screen1"
SCREEN2 = "screen2"
SCREEN3 = "screen3"
state = MENU

# ---------- BUTTONS (rectangles) ----------
btn1 = pygame.Rect(150, 150, 200, 40)
btn2 = pygame.Rect(150, 210, 200, 40)
btn3 = pygame.Rect(150, 270, 200, 40)
back_btn = pygame.Rect(20, 440, 120, 40)

# ---------- MAIN LOOP ----------
running = True
while running:
    clock.tick(60)
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # MENU BUTTONS
            if state == MENU:
                if btn1.collidepoint(mouse):
                    state = SCREEN1
                if btn2.collidepoint(mouse):
                    state = SCREEN2
                if btn3.collidepoint(mouse):
                    state = SCREEN3

            # BACK BUTTON
            if state != MENU:
                if back_btn.collidepoint(mouse):
                    state = MENU

    # ---------- DRAW ----------
    if state == MENU:
        screen.fill((200, 220, 255))  # backdrop 1

        pygame.draw.rect(screen, (180,180,180), btn1)
        pygame.draw.rect(screen, (180,180,180), btn2)
        pygame.draw.rect(screen, (180,180,180), btn3)

        screen.blit(font.render("Screen 1", True, (0,0,0)), (200, 160))
        screen.blit(font.render("Screen 2", True, (0,0,0)), (200, 220))
        screen.blit(font.render("Screen 3", True, (0,0,0)), (200, 280))

    elif state == SCREEN1:
        screen.fill((255, 200, 200))  # backdrop 2
        pygame.draw.rect(screen, (150,150,150), back_btn)
        screen.blit(font.render("BACK", True, (0,0,0)), (50, 450))

    elif state == SCREEN2:
        screen.fill((200, 255, 200))  # backdrop 3
        pygame.draw.rect(screen, (150,150,150), back_btn)
        screen.blit(font.render("BACK", True, (0,0,0)), (50, 450))

    elif state == SCREEN3:
        screen.fill((200, 200, 255))  # backdrop 4
        pygame.draw.rect(screen, (150,150,150), back_btn)
        screen.blit(font.render("BACK", True, (0,0,0)), (50, 450))

    pygame.display.flip()

pygame.quit()


