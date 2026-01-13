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
# -----------------------------------------------------------------------------
# Fancy Gamestate Menu Lab (student-style)
# by: a junior coder (you!)
#
# What I changed (kept functions the same):
# - Added a simple animated "plaid" background (easy to understand)
# - Fancy header/title banner and a short student-style comment block
# - Rounded, shadowed buttons with hover (mouseover) effects
# - Button highlight + slight scale to show interaction (collision detection style)
# - Added a 4th screen (Level 4 requirement)
# - Added ESC key to return to menu for convenience
#
# How to use: Install pygame (pip install pygame), then run this file.
# The program still uses simple rectangle collision for clicks so it's easy to follow.
# -----------------------------------------------------------------------------

import pygame
import sys
import math

pygame.init()

# ---------- SETUP ----------
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
BIG = pygame.font.SysFont(None, 44)

# ---------- GAME STATES ----------
MENU = "menu"
SCREEN1 = "screen1"
SCREEN2 = "screen2"
SCREEN3 = "screen3"
SCREEN4 = "screen4"  # new screen added
state = MENU

# draw---
btn_w, btn_h = 240, 48
btn1 = pygame.Rect((WIDTH - btn_w) // 2, 150, btn_w, btn_h)
btn2 = pygame.Rect((WIDTH - btn_w) // 2, 210, btn_w, btn_h)
btn3 = pygame.Rect((WIDTH - btn_w) // 2, 270, btn_w, btn_h)
btn4 = pygame.Rect((WIDTH - btn_w) // 2, 330, btn_w, btn_h)  # extra button
back_btn = pygame.Rect(20, 440, 120, 40)

# Colors (named so it's easy to change)
BG_COLOR = (220, 230, 255)
BUTTON_COLOR = (200, 200, 200)
BUTTON_HOVER = (170, 180, 220)
SHADOW = (50, 50, 60)
TITLE_COLOR = (20, 20, 60)

# ---------- HELPERS ----------

def draw_plaid(surface, t):
    surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    # vertical bars
    spacing = 36
    offset = int((t * 40) % spacing)
    for x in range(-spacing, WIDTH + spacing, spacing):
        r = pygame.Rect(x + offset, 0, spacing // 3, HEIGHT)
        pygame.draw.rect(surf, (200, 220, 255, 90), r)

    # horizontal bars on another transparent surface for depth
    surf2 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    offset2 = int((t * 30) % spacing)
    for y in range(-spacing, HEIGHT + spacing, spacing):
        r = pygame.Rect(0, y + offset2, WIDTH, spacing // 4)
        pygame.draw.rect(surf2, (230, 200, 210, 70), r)

    surface.blit(surf, (0, 0))
    surface.blit(surf2, (0, 0))


def draw_button(surface, rect, text, is_hover, font, scale=1.0):
    w, h = rect.w * scale, rect.h * scale
    x = rect.centerx - w / 2
    y = rect.centery - h / 2
    scaled = pygame.Rect(int(x), int(y), int(w), int(h))

    # shadow
    shadow_rect = scaled.copy()
    shadow_rect.x += 4
    shadow_rect.y += 6
    pygame.draw.rect(surface, SHADOW, shadow_rect, border_radius=12)

    # color depends on hover
    color = BUTTON_HOVER if is_hover else BUTTON_COLOR
    pygame.draw.rect(surface, color, scaled, border_radius=12)

    # outline
    pygame.draw.rect(surface, (120, 120, 140), scaled, width=2, border_radius=12)

    # text
    text_surf = font.render(text, True, (10, 10, 10))
    text_rect = text_surf.get_rect(center=scaled.center)
    surface.blit(text_surf, text_rect)


def is_hover(rect, mouse_pos):
    return rect.collidepoint(mouse_pos)


# ---------- MAIN LOOP ----------
running = True
start_time = pygame.time.get_ticks() / 1000.0

while running:
    dt = clock.tick(60) / 1000.0
    t = pygame.time.get_ticks() / 1000.0 - start_time
    mouse = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state = MENU

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # handle clicks per state (collision detection style)
            if state == MENU:
                if btn1.collidepoint(mouse):
                    state = SCREEN1
                elif btn2.collidepoint(mouse):
                    state = SCREEN2
                elif btn3.collidepoint(mouse):
                    state = SCREEN3
                elif btn4.collidepoint(mouse):
                    state = SCREEN4
            else:
                if back_btn.collidepoint(mouse):
                    state = MENU

    # ---------- DRAW ----------
    screen.fill(BG_COLOR)
    draw_plaid(screen, t)

    # header/title area
    header_rect = pygame.Rect(0, 10, WIDTH, 90)
    pygame.draw.rect(screen, (255, 255, 255, 40), header_rect)  # subtle strip
    title = BIG.render("Oscar Menu", True, TITLE_COLOR)
    subtitle = font.render("Oscar Hou", True, TITLE_COLOR)
    screen.blit(title, (20, 18))
    screen.blit(subtitle, (20, 56))

    if state == MENU:
        # draw buttons with hover effect and slight scaling when hovered
        hover1 = is_hover(btn1, mouse)
        hover2 = is_hover(btn2, mouse)
        hover3 = is_hover(btn3, mouse)
        hover4 = is_hover(btn4, mouse)

        # use a small pulsing scale when hovered to make it lively
        pulse = 1.0 + 0.03 * math.sin(t * 8)
        draw_button(screen, btn1, "Screen 1", hover1, font, scale=(pulse if hover1 else 1.0))
        draw_button(screen, btn2, "Screen 2", hover2, font, scale=(pulse if hover2 else 1.0))
        draw_button(screen, btn3, "Screen 3", hover3, font, scale=(pulse if hover3 else 1.0))
        draw_button(screen, btn4, "Extra: Screen 4", hover4, font, scale=(pulse if hover4 else 1.0))

        # small footer text for student-style credits
        footer = font.render("Made by Oscar Hou", True, (60, 60, 80))
        screen.blit(footer, (12, HEIGHT - 26))

    else:
        # different simple backdrops for each screen (level requirement)
        if state == SCREEN1:
            screen.fill((255, 230, 230))
            msg = "i am oscar Hou"
        elif state == SCREEN2:
            screen.fill((230, 255, 230))
            msg = "This is my lab"
        elif state == SCREEN3:
            screen.fill((230, 230, 255))
            msg = "It is meet level 4+"
        elif state == SCREEN4:
            screen.fill((250, 245, 220))
            msg = "This is my lab hahahahah"
        else:
            msg = "Unknown"

        # reapply a light plaid overlay so the background keeps the same feel
        draw_plaid(screen, t * 0.6)

        # screen title and a back button
        title_surf = BIG.render(msg, True, TITLE_COLOR)
        title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        screen.blit(title_surf, title_rect)

        # draw back button (with hover)
        back_hover = is_hover(back_btn, mouse)
        draw_button(screen, back_btn, "BACK", back_hover, font, scale=(1.05 if back_hover else 1.0))

        # hint
        hint = font.render("Press ESC to return to menu", True, (80, 80, 110))
        screen.blit(hint, (WIDTH - 220, HEIGHT - 28))

    pygame.display.flip()

pygame.quit()
sys.exit()
