import pygame

pygame.init()
sorting_name_list = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort"]

# Draw the info in popup window
def draw_interface(draw_config, algo_name, is_ascending):
    draw_config.window.fill(draw_config.BG_COLOR)

    if algo_name in sorting_name_list:
        title = draw_config.LARGE_FONT.render(f"{algo_name} - {'Ascending' if is_ascending else 'Descending'}", 1, draw_config.GREEN)
        draw_config.window.blit(title, (draw_config.width / 2 - title.get_width() / 2, 5))
    else:
        title = draw_config.LARGE_FONT.render(f"{algo_name}", 1, draw_config.GREEN)
        draw_config.window.blit(title, (draw_config.width / 2 - title.get_width() / 2, 5))
    
    controls = draw_config.STANDARD_FONT.render("R - Reset | SPACE - Start | A - Ascend | D - Descend", 1, draw_config.BLACK)
    draw_config.window.blit(controls, (draw_config.width / 2 - controls.get_width() / 2, 45))

    sort_options = draw_config.STANDARD_FONT.render("B - Bubble | I - Insertion | S - Selection | Q - Quick Sort", 1, draw_config.BLACK)
    draw_config.window.blit(sort_options, (draw_config.width / 2 - sort_options.get_width() / 2, 75))

    sort_options = draw_config.STANDARD_FONT.render("L - Linear Search | M - Binary Search", 1, draw_config.BLACK)
    draw_config.window.blit(sort_options, (draw_config.width / 2 - sort_options.get_width() / 2, 105))

    draw_bars(draw_config)
    pygame.display.update()


def draw_bars(draw_config, color_positions=None, clear_background=False):
    if color_positions is None:
        color_positions = {}

    if clear_background:
        clear_rect = (draw_config.MARGIN_HORIZONTAL // 2, draw_config.MARGIN_TOP, draw_config.width - draw_config.MARGIN_HORIZONTAL, draw_config.height - draw_config.MARGIN_TOP)
        pygame.draw.rect(draw_config.window, draw_config.BG_COLOR, clear_rect)

    # Define font for drawing numeric values
    value_font = pygame.font.SysFont('comicsans', 15)  # Smaller font for numbers

    for index, value in enumerate(draw_config.list_values):
        x = draw_config.start_x + index * draw_config.bar_width
        y = draw_config.height -  (value - draw_config.min_value) * draw_config.bar_height
        color = draw_config.COLOR_GRADIENTS[index % 3]
        if index in color_positions:
            color = color_positions[index]

        # Draw the bar
        pygame.draw.rect(draw_config.window, color, (x, y, draw_config.bar_width, draw_config.height - y))

        # Render the text for the bar value
        value_text = value_font.render(str(value), True, draw_config.BLACK)
        text_x = x + (draw_config.bar_width // 2) - (value_text.get_width() // 2)
        text_y = y - value_text.get_height()

        # Place text on top of each bar
        if text_y < 0:
            text_y = y + 1

        draw_config.window.blit(value_text, (text_x, text_y))

    if clear_background:
        pygame.display.update()