import pygame
import math

pygame.init()

class VisualizationConfig:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GREY = (128, 128, 128)
    LIGHT_BLUE = (72, 189, 187)
    BG_COLOR = WHITE  # Background color
    
    COLOR_GRADIENTS = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]
    STANDARD_FONT = pygame.font.SysFont('comicsans', 20)
    LARGE_FONT = pygame.font.SysFont('comicsans', 23)

    MARGIN_HORIZONTAL = 100
    MARGIN_TOP = 150

    def __init__(self, width, height, list_values):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.update_list(list_values)
    
    def update_list(self, list_values):
        self.list_values = list_values
        self.min_value = min(list_values)
        self.max_value = max(list_values)
        self.bar_width = round((self.width - self.MARGIN_HORIZONTAL) / len(list_values))
        self.bar_height = math.floor((self.height - self.MARGIN_TOP) / (self.max_value - self.min_value))
        self.start_x = self.MARGIN_HORIZONTAL // 2