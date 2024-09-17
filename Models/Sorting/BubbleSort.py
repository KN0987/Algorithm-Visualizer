from Controllers.DrawConfig import draw_bars

def bubble_sort(vis_config, ascending=True):
    list_values = vis_config.list_values
    for i in range(len(list_values) - 1):
        for j in range(len(list_values) - 1 - i):
            if (list_values[j] > list_values[j + 1] and ascending) or (list_values[j] < list_values[j + 1] and not ascending):
                list_values[j], list_values[j + 1] = list_values[j + 1], list_values[j]
                draw_bars(vis_config, {j: vis_config.GREEN, j + 1: vis_config.RED}, True)
                yield True
    return list_values