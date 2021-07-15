# pygame
import pygame
import pygame.key
from pygame.locals import *
# rich
from rich.console import Console

# Console
console = Console()

# Extension Details
console.print("\nUsing Pygame Movement Extension", style="bold green")

# Movement Class


class Movement():
    def __init__(self, character, speed, window_width, window_height):
        # Character for movement
        self.character = character

        # Speed for character
        self.speed = speed

        # width and height of window
        self.width = window_width
        self.height = window_height

        # Getting pressed keys
        self.keys_pressed = pygame.key.get_pressed()

    # Movement with WASD keys
    def wasd(self):
        # Looking for errors
        try:
            # W - Upper side movement
            if self.keys_pressed[K_w] and self.character.y - self.speed > 0:
                self.character.y -= self.speed

            # S - Bottom side movement
            if self.keys_pressed[K_s] and self.character.y + self.speed + self.character.get_height() < self.height:
                self.character.y += self.speed

            # A - Left side movement
            if self.keys_pressed[K_a] and self.character.x + self.speed > self.speed + 5:
                self.character.x -= self.speed

            # D - Right side movement
            if self.keys_pressed[K_d] and self.character.x + self.speed + self.character.get_width() < self.width + 5:
                self.character.x += self.speed

        # Handling errors
        except:
            # Printing Error
            console.print(
                "\nCant exhibit movement , please check the arguments !\n", style="bold red")
            # Exiting
            exit()

    # Movement with ARROW keys
    def arrows(self):
        # Looking for errors
        try:
            # UP - Upper side movement
            if self.keys_pressed[K_UP] and self.character.y - self.speed > 0:
                self.character.y -= self.speed

            # DOWN - Bottom side movement
            if self.keys_pressed[K_DOWN] and self.character.y + self.speed + self.character.get_height() < self.height:
                self.character.y += self.speed

            # LEFT - Left side movement
            if self.keys_pressed[K_LEFT] and self.character.x + self.speed > self.speed:
                self.character.x -= self.speed

            # RIGHT - Right side movement
            if self.keys_pressed[K_RIGHT] and self.character.x + self.speed + self.character.get_width() < self.width + 5:
                self.character.x += self.speed

        # Handling errors
        except:
            # Printing Error
            console.print(
                "\nCant exhibit movement , please check the arguments !\n", style="bold red")
            # Exiting
            exit()


# printing engine
if __name__ == "__main__":
    console.print("\nPygame Movement Extension\n", style="bold green")
