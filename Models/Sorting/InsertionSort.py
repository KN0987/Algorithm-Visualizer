from Controllers.DrawConfig import draw_bars

def insertion_sort(vis_config, ascending=True):
    list_values = vis_config.list_values
    for i in range(1, len(list_values)):
        current = list_values[i]
        while True:
            should_sort = (i > 0 and list_values[i - 1] > current and ascending) or (i > 0 and list_values[i - 1] < current and not ascending)
            if not should_sort:
                break
            list_values[i] = list_values[i - 1]
            i -= 1
            list_values[i] = current
            draw_bars(vis_config, {i - 1: vis_config.GREEN, i: vis_config.RED}, True)
            yield True
    return list_values