# -----------------------------------------------------------------------------
# TEXT & FONT LAB - RANSOM NOTE
# 
# Use your new knowledge of text in Pygame to make a ransom note similar to the picture above.
# 
# You use whatever fonts you want as long as you use at least 1 custom font.
# 
# The message can say whatever you want as long as it is school safe (remember the code of conduct).
# 
# Lab Requirements:
# LEVEL 3
# Use at least 3 different font styles
# Use 3 different colours
# Write a message that is school safe and does not have anyone’s personal information (including names)

# LEVEL 4
# Everything listed in level 3 
# Use at least 4 different font styles
# Use 4 different colours

# LEVEL 4+
# Everything listed in level 4
# Use a custom downloaded font
# 
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# Pygame Text & Fonts
# 
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
import os

pygame.init()
pygame.font.init()

# Window setup
W, H = 700, 500
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pygame Ransom Note")
clock = pygame.time.Clock()

# Message (school-safe)
message = "SURPRISE PARTY TONIGHT!"

# Colour palette (at least 4)
COLORS = [
    (200, 30, 45),   # red
    (35, 95, 185),   # blue
    (40, 160, 60),   # green
    (140, 30, 150),  # purple
    (240, 140, 20),  # orange (extra)
]

# Font names to try for system fonts (variety of styles)
SYS_FONT_NAMES = ["arial", "timesnewroman", "comicsansms", "couriernew", "verdana"]

# Custom font filename (place your downloaded .ttf here if you want Level 4+)
CUSTOM_FONT_FILE = "custom_font.ttf"
custom_font_exists = os.path.isfile(CUSTOM_FONT_FILE)

# Helper to create a pygame Font object. If custom font exists, sometimes use it.
def make_font(size, prefer_custom=False):
    if prefer_custom and custom_font_exists:
        try:
            return pygame.font.Font(CUSTOM_FONT_FILE, size)
        except Exception:
            pass
    # pick a random system font from the list (pygame will fallback if name not found)
    name = random.choice(SYS_FONT_NAMES)
    return pygame.font.SysFont(name, size)

# Generate positions and letter surfaces for the ransom-note layout
def create_ransom_surfaces(text, max_width, line_spacing=10):
    pieces = []  # list of (surface, pos)
    x = 20
    y = 40
    for ch in text:
        if ch == " ":
            x += random.randint(12, 24)  # spacing for space
            continue

        # Choose whether to use custom font for this character sometimes
        prefer_custom = random.random() < 0.35  # 35% chance to use custom font if available

        size = random.randint(28, 64)  # varied sizes
        font = make_font(size, prefer_custom=prefer_custom)

        color = random.choice(COLORS)
        # render letter; True for antialias
        surf = font.render(ch, True, color)

        # add small border effect (draw a faint shadow by blitting offset black)
        shadow = pygame.Surface((surf.get_width()+2, surf.get_height()+2), pygame.SRCALPHA)
        shadow.fill((0,0,0,0))
        # light shadow
        shadow.blit(font.render(ch, True, (20,20,20)), (2,2))
        shadow.blit(surf, (0,0))
        surf = shadow

        # rotate for ransom look
        angle = random.randint(-35, 35)
        surf = pygame.transform.rotate(surf, angle)

        # if out of width, move to next line
        w = surf.get_width()
        h = surf.get_height()
        if x + w > max_width - 20:
            x = 20
            y += h + line_spacing + random.randint(0, 12)

        # tiny vertical jitter
        pos = (x + random.randint(-6, 6), y + random.randint(-6, 6))

        pieces.append((surf, pos))
        x += w + random.randint(6, 18)

    return pieces

# Create initial layout
pieces = create_ransom_surfaces(message, W)

# Simple button to regenerate layout with new randomization when user presses R
def regenerate():
    global pieces
    pieces = create_ransom_surfaces(message, W)

# Main loop
running = True
bg_color = (245, 235, 215)  # warm paper-like background
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_r:
                regenerate()
            elif ev.key == pygame.K_s:
                # save a screenshot
                fname = "ransom_screenshot.png"
                pygame.image.save(window, fname)
                print(f"Saved screenshot to {fname}")

    window.fill(bg_color)

    # draw a torn-paper rectangle for flair
    paper_rect = pygame.Rect(10, 10, W - 20, H - 20)
    pygame.draw.rect(window, (255, 255, 250), paper_rect)  # slightly off-white paper
    pygame.draw.rect(window, (150, 120, 80), paper_rect, 3)  # border

    # draw each letter piece
    for surf, pos in pieces:
        window.blit(surf, pos)

    # small legend / instructions
    info_font = pygame.font.SysFont("arial", 14)
    info_surf = info_font.render("Press R to reshuffle letters  |  Press S to save screenshot", True, (60,60,60))
    window.blit(info_surf, (10, H - 28))

    # If custom font not found, show a gentle reminder
    if not custom_font_exists:
        warn = info_font.render("Note: custom_font.ttf not found — place a .ttf named 'custom_font.ttf' in this folder to use a custom font.", True, (120,20,20))
        window.blit(warn, (10, H - 48))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


