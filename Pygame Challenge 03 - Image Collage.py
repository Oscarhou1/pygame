# -----------------------------------------------------------------------------
# IMAGE LAB - IMAGE COLLAGE
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# Use at least 3 different images to create a collage
# You can repeat the same images must use other commands to change the look (example, tint)

# LEVEL 4
# Everything listed in level 3 
# Create a scene with images

# LEVEL 4+
# Everything listed in level 4
# Randomize or animate something

# Recommended Lessons:
# P5.js intro
# P5.js drawing
# P5.js colour
# 
# Challenge Difficulty:**
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to githun when finished
# 
# Good luck!
#-----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMAGE LAB - IMAGE COLLAGE
#
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
#
# Lab Requirements:
# LEVEL 3
# Use at least 3 different images to create a collage
# You can repeat the same images must use other commands to change the look (example, tint)

# LEVEL 4
# Everything listed in level 3
# Create a scene with images

# LEVEL 4+
# Everything listed in level 4
# Randomize or animate something

# Recommended Lessons:
# P5.js intro
# P5.js drawing
# P5.js colour
#
# Challenge Difficulty:**
#
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
#
# Upload your code to githun when finished
#
# Good luck!
# -----------------------------------------------------------------------------
# pygame_image_collage.py
# Pygame Image Collage — Level 4+
# - Creates 3 different "images" (pygame.Surface objects drawn in code)
# - Uses them multiple times with transforms (scale, rotate, tint)
# - Creates a scene (background + ground + sky)
# - Animates images and randomizes on mouse click

import pygame
import sys
import math
import random

pygame.init()
WINDOW_W, WINDOW_H = 800, 600
window = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("Image Collage - Pygame Lab (Level 4+)")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 16)

# ---------- Helper: create "image" surfaces ----------
def create_circle_image(radius=50):
    """Create an image made of concentric circles (looks like a flower)."""
    surf = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
    cx, cy = radius, radius
    for i, r in enumerate(range(radius, 0, -8)):
        color = (255 - i*20, 120 + i*10 % 135, 190 - i*10, 255 - i*10)  # RGBA
        pygame.draw.circle(surf, color, (cx, cy), r)
    # Add a center dot
    pygame.draw.circle(surf, (255, 230, 0), (cx, cy), max(6, radius//8))
    return surf

def create_triangle_image(size=110):
    """Create an image with a triangle and details (looks like a pennant)."""
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    pts = [(10, size-10), (size-10, size//2), (10, 10)]
    pygame.draw.polygon(surf, (50, 150, 230), pts)
    pygame.draw.polygon(surf, (255,255,255,60), [(12, size-12), (size-12, size//2), (12, 12)])
    # small detail
    for i in range(5):
        pygame.draw.circle(surf, (255,255,255,50), (size//2, size//2 - i*8), 3)
    return surf

def create_face_image(w=90, h=90):
    """Create a simple face-like image (cute character)."""
    surf = pygame.Surface((w,h), pygame.SRCALPHA)
    pygame.draw.ellipse(surf, (240,200,170), (0,0,w,h))  # head
    # eyes
    pygame.draw.circle(surf, (30,30,30), (w//3, h//3), 6)
    pygame.draw.circle(surf, (30,30,30), (2*w//3, h//3), 6)
    # blush
    pygame.draw.circle(surf, (255,120,120,140), (w//3, h//2), 10)
    pygame.draw.circle(surf, (255,120,120,140), (2*w//3, h//2), 10)
    # smile
    pygame.draw.arc(surf, (150,60,60), (w//4, h//3, w//2, h//2), math.pi/8, math.pi-math.pi/8, 3)
    return surf

# Create three different "images"
img_flower = create_circle_image(60)
img_pennant = create_triangle_image(120)
img_face = create_face_image(92,92)

# ---------- Collage items: each item is an instance of an image with props ----------
class CollageItem:
    def __init__(self, image, x, y, scale=1.0, angle=0.0, vx=0, vy=0):
        self.base_image = image
        self.x = x
        self.y = y
        self.scale = scale
        self.angle = angle
        self.vx = vx
        self.vy = vy
        self.float_offset = random.random()*100  # for per-item sine movement
        self.tint = None  # (r,g,b,a) or None

    def get_transformed(self):
        # scale
        size = self.base_image.get_size()
        new_size = (max(1, int(size[0]*self.scale)), max(1, int(size[1]*self.scale)))
        surf = pygame.transform.smoothscale(self.base_image, new_size)
        # rotate
        surf = pygame.transform.rotate(surf, self.angle)
        # apply tint if present (multiply)
        if self.tint:
            tint_surf = pygame.Surface(surf.get_size(), pygame.SRCALPHA)
            tint_surf.fill(self.tint)
            surf.blit(tint_surf, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
        return surf

    def update(self, dt, t):
        # slight floating motion
        self.y += math.sin((t + self.float_offset) * 0.8) * 0.2 * dt
        self.x += math.cos((t + self.float_offset) * 0.6) * 0.15 * dt
        # velocity
        self.x += self.vx * dt
        self.y += self.vy * dt
        # keep inside screen (wrap)
        if self.x < -200: self.x = WINDOW_W + 200
        if self.x > WINDOW_W + 200: self.x = -200
        if self.y < -200: self.y = WINDOW_H + 200
        if self.y > WINDOW_H + 200: self.y = -200

    def draw(self, target):
        surf = self.get_transformed()
        rect = surf.get_rect(center=(int(self.x), int(self.y)))
        target.blit(surf, rect)

# Build a scene with multiple instances: some repeated using transforms
items = []
random.seed(42)

# place multiple flowers, faces, pennants with variations
for i in range(6):
    items.append(CollageItem(img_flower,
                             x=random.randint(60, WINDOW_W-60),
                             y=random.randint(60, WINDOW_H-200),
                             scale=random.uniform(0.6,1.2),
                             angle=random.uniform(0,360),
                             vx=random.uniform(-0.02,0.02),
                             vy=random.uniform(-0.01,0.01)))
for i in range(5):
    items.append(CollageItem(img_pennant,
                             x=random.randint(40, WINDOW_W-40),
                             y=random.randint(WINDOW_H-220, WINDOW_H-80),
                             scale=random.uniform(0.4,1.0),
                             angle=random.uniform(-40,40),
                             vx=random.uniform(-0.03,0.03),
                             vy=random.uniform(-0.015,0.015)))
for i in range(7):
    items.append(CollageItem(img_face,
                             x=random.randint(40, WINDOW_W-40),
                             y=random.randint(40, WINDOW_H-140),
                             scale=random.uniform(0.5,1.0),
                             angle=random.uniform(-20,20),
                             vx=random.uniform(-0.02,0.02),
                             vy=random.uniform(-0.018,0.018)))

# Add a couple of larger foreground repeats to show transform effects
items.append(CollageItem(img_flower, x=WINDOW_W*0.15, y=WINDOW_H*0.75, scale=1.6, angle=0))
items.append(CollageItem(img_face, x=WINDOW_W*0.85, y=WINDOW_H*0.7, scale=1.4, angle=-18))

# ---------- Utility functions ----------
def randomize_tints():
    """Randomize tints for each item to demonstrate 'tint' image alteration."""
    for it in items:
        # 50% chance to tint
        if random.random() < 0.6:
            r = random.randint(120,255)
            g = random.randint(120,255)
            b = random.randint(120,255)
            a = random.randint(180,255)
            it.tint = (r,g,b,a)
        else:
            it.tint = None

def shuffle_positions():
    for it in items:
        it.x = random.randint(-20, WINDOW_W+20)
        it.y = random.randint(-20, WINDOW_H+20)
        it.vx = random.uniform(-0.03,0.03)
        it.vy = random.uniform(-0.02,0.02)

# initial randomization
randomize_tints()

# ---------- Main loop ----------
running = True
t = 0.0
while running:
    dt_ms = clock.tick(60)
    dt = dt_ms / 16.6667  # normalized to ~60fps steps (so motion is framerate-tolerant)
    t += dt * 0.016  # smaller time scale for sine motion

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                running = False
            elif ev.key == pygame.K_r:
                # press R to randomize tints
                randomize_tints()
            elif ev.key == pygame.K_s:
                # press S to shuffle positions
                shuffle_positions()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            # left click randomizes colors / right click shuffles positions
            if ev.button == 1:
                randomize_tints()
            elif ev.button == 3:
                shuffle_positions()

    # ---------- Update ----------
    for it in items:
        # slowly rotate a few items for variety
        it.angle += 0.06 * dt  # degrees per normalized step
        it.update(dt, t)

    # ---------- Draw Scene ----------
    # sky gradient (simple)
    for y in range(WINDOW_H):
        # gradient from light blue at top to pale at bottom
        frac = y / WINDOW_H
        r = int(120 + 80 * frac)
        g = int(190 + 50 * frac)
        b = int(255 - 60 * frac)
        pygame.draw.line(window, (r,g,b), (0,y),(WINDOW_W,y))

    # ground
    pygame.draw.rect(window, (40,120,60), (0, WINDOW_H-140, WINDOW_W, 140))
    # distant hills
    pygame.draw.ellipse(window, (30,90,50), (-200, WINDOW_H-260, 600, 220))
    pygame.draw.ellipse(window, (35,100,55), (180, WINDOW_H-260, 700, 220))

    # sun (background)
    pygame.draw.circle(window, (255,230,100,160), (WINDOW_W-120, 80), 50)

    # Draw collage items (some z-ordering: back-to-front)
    # draw lower items first (pennants near ground), then others
    for it in sorted(items, key=lambda a: a.y):
        it.draw(window)

    # overlay: repeated pattern to create "collage" feel (repeating same image with tint/scale)
    # repeat a small version of the pennant across the top edge
    small = pygame.transform.smoothscale(img_pennant, (60,60))
    for i in range(0, WINDOW_W, 80):
        window.blit(small, (i+10, 10 + (i//80 % 2)*6), special_flags=pygame.BLEND_PREMULTIPLIED)

    # instructions UI
    info_lines = [
        "Image Collage Lab - Level 4+",
        "Left click: randomize tints  |  Right click: shuffle positions",
        "Keys: R = randomize tints, S = shuffle positions, ESC = quit",
        "This program uses 3 unique image surfaces (flower, pennant, face), repeated & transformed.",
    ]
    y0 = 8
    for line in info_lines:
        txt = FONT.render(line, True, (15,15,15))
        # draw background rectangle for legibility
        bg = pygame.Surface((txt.get_width()+8, txt.get_height()+4), pygame.SRCALPHA)
        bg.fill((255,255,255,200))
        window.blit(bg, (8, y0-2))
        window.blit(txt, (12, y0))
        y0 += txt.get_height() + 6

    pygame.display.flip()

pygame.quit()
sys.exit()


