from Controllers.DrawConfig import draw_bars

def linear_search(vis_config, target):
    # Perform a linear search; the function yields at each comparison
    list_values = vis_config.list_values
    for index, value in enumerate(list_values):
        draw_bars(vis_config, {index: vis_config.RED}, True)
        if value == target:
            draw_bars(vis_config, {index: vis_config.GREEN}, True)
            yield index
            return   # Found the target, yield the index
        yield None
    yield -1

def binary_search(vis_config, target):
    list_values = vis_config.list_values
    low, high = 0, len(list_values) - 1

    while low <= high:
        mid = (low + high) // 2

        # Draw the current low and high indices in red
        draw_bars(vis_config, {low: vis_config.RED, high: vis_config.RED}, True)
        
        if list_values[mid] == target:
            draw_bars(vis_config, {mid: vis_config.GREEN}, True)  # Highlight mid in green when target is found
            yield mid
            return
        
        elif list_values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        
        yield None
    
    yield -1
