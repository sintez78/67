import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))

COLORS = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'gray': (200, 200, 200)
}

def draw_body(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_head(surface, x, y, size, color):
    circle(surface, color, (x, y), size // 2)

def draw_ear(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_leg(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_eye(surface, x, y, size):
    circle(surface, COLORS['white'], (x, y), size // 2)
    circle(surface, COLORS['black'], (x, y), size // 4)  

def draw_mouth(surface, x, y, size):
    pygame.draw.arc(surface, COLORS['black'], 
                    (x - size // 2, y - size // 4, size, size // 2), 
                    0, math.pi, 1)

def draw_whisker(surface, x, y, length, angle, direction):
    if direction == "left":
        end_x = x - length * math.cos(angle)
    else:
        end_x = x + length * math.cos(angle)
    end_y = y - length * math.sin(angle)
    line(surface, COLORS['black'], (x, y), (end_x, end_y), 1)

def draw_whiskers_set(surface, x, y, length, direction):
    angles = [0.3, 0.5, 0.4]
    y_offsets = [0, 0, -2]
    
    for angle, y_offset in zip(angles, y_offsets):
        draw_whisker(surface, x, y + y_offset, length, angle, direction)

def draw_hare(surface, x, y, width, height, color):
    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2
    draw_body(surface, x, body_y, body_width, body_height, color)
    
    head_size = height // 4
    head_y = y - head_size // 2
    draw_head(surface, x, head_y, head_size, color)
    
    eye_size = head_size // 4
    eye_y = head_y - head_size // 8
    draw_eye(surface, x - head_size // 4, eye_y, eye_size)
    draw_eye(surface, x + head_size // 4, eye_y, eye_size)
    
    mouth_y = head_y + head_size // 6
    draw_mouth(surface, x, mouth_y, head_size // 3)
    
    whisker_y = head_y + head_size // 8
    whisker_length = head_size // 2
    
    draw_whiskers_set(surface, x - head_size // 5, whisker_y, whisker_length, "left")
    draw_whiskers_set(surface, x + head_size // 5, whisker_y, whisker_length, "right")
    
    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    for ear_x in (x - head_size // 4, x + head_size // 4):
        draw_ear(surface, ear_x, ear_y, width // 8, ear_height, color)
    
    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    for leg_x in (x - width // 4, x + width // 4):
        draw_leg(surface, leg_x, leg_y, width // 4, leg_height, color)

def main():
    draw_hare(screen, 200, 200, 200, 400, COLORS['gray'])
    pygame.display.update()
    
    clock = pygame.time.Clock()
    finished = False
    
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    
    pygame.quit()

