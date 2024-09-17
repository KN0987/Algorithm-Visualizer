import pygame
from Controllers.DrawConfig import draw_bars

pygame.init()

def quick_sort(vis_config, ascending=True):
    list_values = vis_config.list_values

    def partition(low, high):
        i = low - 1
        pivot = list_values[high]
        for j in range(low, high):
            if (list_values[j] < pivot and ascending) or (list_values[j] > pivot and not ascending):
                i += 1
                list_values[i], list_values[j] = list_values[j], list_values[i]
                draw_bars(vis_config, {i: vis_config.GREEN, j: vis_config.RED}, True)
                yield True
        list_values[i + 1], list_values[high] = list_values[high], list_values[i + 1]
        draw_bars(vis_config, {i + 1: vis_config.GREEN, high: vis_config.RED}, True)
        yield True
        return i + 1

    def recursive_quick_sort(low, high):
        if low < high:
            pi = yield from partition(low, high)
            yield from recursive_quick_sort(low, pi - 1)
            yield from recursive_quick_sort(pi + 1, high)
        
    yield from recursive_quick_sort(0, len(list_values) - 1)
    return list_values