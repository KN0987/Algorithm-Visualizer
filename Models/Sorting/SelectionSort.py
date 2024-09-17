from Controllers.DrawConfig import draw_bars

def selection_sort(vis_config, ascending=True):
    list_values = vis_config.list_values
    for i in range(len(list_values)):
        min_index = i
        for j in range(i + 1, len(list_values)):
            if (list_values[j] < list_values[min_index] and ascending) or (list_values[j] > list_values[min_index] and not ascending):
                min_index = j
        list_values[i], list_values[min_index] = list_values[min_index], list_values[i]
        draw_bars(vis_config, {i: vis_config.GREEN, min_index: vis_config.RED}, True)
        yield True
    return list_values