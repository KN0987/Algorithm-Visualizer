import pygame
import random
from Controllers.VisualizationConfig import VisualizationConfig
from Controllers.DrawConfig import draw_interface
from Models.Sorting.BubbleSort import bubble_sort
from Models.Sorting.InsertionSort import insertion_sort
from Models.Sorting.SelectionSort import selection_sort
from Models.Sorting.QuickSort import quick_sort
from Models.Searching.Searching import linear_search, binary_search

pygame.init()

def generate_list(num_items, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(num_items)]

def main():
    running = True
    clock = pygame.time.Clock()
    

    num_elements = 15
    min_val = 0
    max_val = 100

    list_values = generate_list(num_elements, min_val, max_val)
    visualization_config = VisualizationConfig(1500, 750, list_values)

    sorting_active = False
    sort_ascending = True
    current_algo = bubble_sort
    sorting_gen = None
    
    algo_name = "Bubble Sort"
    
    searching_active = False
    searching_gen = None
    target = list_values[len(list_values)-3]
    print(target)

    while running:
        clock.tick(60)

        if sorting_active or searching_active:
            try:
                if sorting_active:
                    next(sorting_gen)
                elif searching_active:
                    result = next(searching_gen)
                    if result is not None:
                        searching_active = False
                pygame.time.wait(700)
            except StopIteration:
                sorting_active = False
        else:
            draw_interface(visualization_config, algo_name, sort_ascending)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r: 
                list_values = generate_list(num_elements, min_val, max_val)
                visualization_config.update_list(list_values)
                sorting_active = False
                searching_active = False
            elif event.key == pygame.K_SPACE and not sorting_active:
                if algo_name == "Linear Search" or algo_name == "Binary Search":
                    searching_active = True
                    searching_gen = current_algo(visualization_config, target)
                else:
                    sorting_active = True
                    sorting_gen = current_algo(visualization_config, sort_ascending)
            
            if not sorting_active:  
                if event.key == pygame.K_a:
                    sort_ascending = True
                elif event.key == pygame.K_d:
                    sort_ascending = False
                elif event.key == pygame.K_b:
                    current_algo = bubble_sort
                    algo_name = "Bubble Sort"
                elif event.key == pygame.K_i:
                    current_algo = insertion_sort
                    algo_name = "Insertion Sort"
                elif event.key == pygame.K_s:
                    current_algo = selection_sort
                    algo_name = "Selection Sort"
                elif event.key == pygame.K_q:
                    current_algo = quick_sort
                    algo_name = "Quick Sort"
            
            if not searching_active:
                if event.key == pygame.K_l:
                    current_algo = linear_search
                    algo_name = "Linear Search"
                elif event.key == pygame.K_m:
                    list_values.sort()
                    current_algo = binary_search
                    algo_name = "Binary Search"
            

    pygame.quit()

if __name__ == "__main__":
    main()
